import ast
import io
import json
import multiprocessing as mp
import re
import traceback
from contextlib import redirect_stderr, redirect_stdout
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

import torch
from datasets import Dataset
from peft import LoraConfig, PeftModel, get_peft_model
from tqdm import tqdm
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    PrinterCallback,
    ProgressCallback,
)
from trl import GRPOConfig, GRPOTrainer


SYSTEM_PROMPT = """You are solving a Python Programming Puzzle.

The user will provide a Python function named sat(answer).
Your job is to write a zero-argument function named sol that CONSTRUCTS and RETURNS a single answer value.

Important rules:
- sat is already defined by the user; DO NOT redefine sat
- You must define exactly one function named sol
- sol must take NO arguments
- sol must return one answer object
- The final checker will run: assert sat(sol())
- Do NOT write tests
- Do NOT write a main block
- Do NOT print anything
- Do NOT include explanations or comments outside the code
- Do NOT wrap the code in markdown fences

Your output must be valid Python code only.

Correct pattern:
def sol():
    return <answer>

Incorrect pattern:
def sol(x):
    ...
"""


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_default_model(model_id: str = "deepseek-ai/deepseek-coder-1.3b-instruct"):
    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    has_native_chat_template = tokenizer.chat_template is not None

    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        trust_remote_code=True,
        dtype=torch.bfloat16,
        device_map=None,
        low_cpu_mem_usage=True,
    ).to("cuda")

    model.eval()
    return model, tokenizer, has_native_chat_template


def _sandbox_worker(payload: dict, queue):
    try:
        sat_code = payload["sat_code"]
        candidate = payload["candidate"]

        class BlockedIO(io.StringIO):
            def write(self, s):
                return len(s)

        blocked_stdout = BlockedIO()
        blocked_stderr = BlockedIO()

        globals_dict: dict[str, Any] = {
            "__builtins__": __builtins__,
            "Any": Any,
            "Dict": Dict,
            "List": List,
            "Set": Set,
            "Tuple": Tuple,
        }

        with redirect_stdout(blocked_stdout), redirect_stderr(blocked_stderr):
            exec(sat_code, globals_dict, globals_dict)

            sat_fn = globals_dict.get("sat")
            if not callable(sat_fn):
                queue.put({"ok": False, "reason": "sat_not_callable"})
                return

            exec_globals: dict[str, Any] = {
                "__builtins__": __builtins__,
                "sat": sat_fn,
                "Any": Any,
                "Dict": Dict,
                "List": List,
                "Set": Set,
                "Tuple": Tuple,
            }

            exec(candidate, exec_globals, exec_globals)

            sol_fn = exec_globals.get("sol")
            if not callable(sol_fn):
                queue.put({"ok": False, "reason": "sol_not_callable"})
                return

            result = sat_fn(sol_fn())
            queue.put({"ok": True, "result": bool(result)})
    except Exception as exc:
        queue.put(
            {
                "ok": False,
                "reason": f"{type(exc).__name__}: {exc}",
            }
        )


class RewardProgressCallback(ProgressCallback):
    def on_log(self, args, state, control, logs=None, **kwargs):
        if not logs:
            return

        reward = logs.get("reward", logs.get("rewards/_reward_func/mean"))
        reward_std = logs.get("reward_std", logs.get("rewards/_reward_func/std"))

        if reward is None:
            return

        if self.training_bar is not None:
            if reward_std is None:
                self.training_bar.write(f"Reward: {float(reward):.3f}")
            else:
                self.training_bar.write(
                    f"Reward: {float(reward):.3f}±{float(reward_std):.3f}"
                )


class LadderOptimizer:
    def __init__(
        self,
        model,
        tokenizer,
        run_dir: Path,
        debug: bool = False,
        has_native_chat_template: bool | None = None,
        exec_timeout_seconds: float = 1.0,
    ):
        self.model = model
        self.tokenizer = tokenizer
        self.run_dir = Path(run_dir)
        self.trainer = None
        self.debug = debug
        self.difficulty_order = ["easy", "medium", "hard"]
        self.exec_timeout_seconds = exec_timeout_seconds
        self._peft_initialized = isinstance(model, PeftModel)

        if has_native_chat_template is None:
            has_native_chat_template = tokenizer.chat_template is not None
        self.has_native_chat_template = has_native_chat_template

    def _warn(self, message: str):
        print(f"[WARN] {message}")

    def _build_plain_prompt(self, sat_code: str) -> str:
        return (
            f"{SYSTEM_PROMPT}\n\n"
            f"Here is the puzzle:\n"
            f"{sat_code}\n\n"
            f"Write Python code that defines only sol(), where sol takes no arguments "
            f"and returns an answer such that sat(sol()) is True.\n"
            f"Output only code.\n"
        )

    def _build_prompt_representation(self, sat_code: str):
        if self.has_native_chat_template:
            return [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": sat_code},
            ]
        return self._build_plain_prompt(sat_code)

    def _strip_code_fences(self, text: str) -> tuple[str, float]:
        penalty = 0.0
        cleaned = text.strip()

        if cleaned.startswith("```python"):
            cleaned = cleaned[len("```python") :].strip()
            penalty += 0.05
        elif cleaned.startswith("```"):
            cleaned = cleaned[3:].strip()
            penalty += 0.05

        if cleaned.endswith("```"):
            cleaned = cleaned[:-3].strip()
            penalty += 0.05

        return cleaned, penalty

    def _pretty_debug_block(self, title: str, text: str):
        width = 24
        print(f"\n{'=' * width} {title} {'=' * width}")
        print(text)
        print(f"{'=' * (width * 2 + len(title) + 2)}\n")

    def _decode_generated_completion(self, inputs, output_ids) -> str:
        prompt_len = inputs["input_ids"].shape[1]
        completion_ids = output_ids[0][prompt_len:]
        return self.tokenizer.decode(completion_ids, skip_special_tokens=True).strip()

    def _summarize_text(self, text: str, max_len: int = 100) -> str:
        one_line = " ".join(text.strip().split())
        if len(one_line) <= max_len:
            return one_line
        return one_line[: max_len - 3] + "..."

    def _extract_code_block(self, text: str) -> tuple[str, dict]:
        details = {
            "had_fence": False,
            "fence_type": "none",
            "had_preamble": False,
            "start_offset": -1,
        }

        text = text.strip()

        fenced = re.search(r"```python\s*(.*?)```", text, re.DOTALL | re.IGNORECASE)
        if fenced:
            details["had_fence"] = True
            details["fence_type"] = "python"
            details["had_preamble"] = fenced.start() > 0 and bool(text[: fenced.start()].strip())
            details["start_offset"] = fenced.start()
            return fenced.group(1).strip(), details

        fenced = re.search(r"```\s*(.*?)```", text, re.DOTALL)
        if fenced:
            details["had_fence"] = True
            details["fence_type"] = "generic"
            details["had_preamble"] = fenced.start() > 0 and bool(text[: fenced.start()].strip())
            details["start_offset"] = fenced.start()
            return fenced.group(1).strip(), details

        details["had_preamble"] = bool(text and not text.startswith("def sol"))
        return text, details

    def _candidate_prefixes(self, text: str) -> tuple[list[str], dict]:
        code_text, extraction = self._extract_code_block(text)

        start = code_text.find("def sol")
        extraction["found_def_sol"] = start != -1
        extraction["sol_start_after_extraction"] = start

        if start == -1:
            extraction["candidate_count"] = 0
            return [], extraction

        code_text = code_text[start:].strip()
        lines = code_text.splitlines()

        candidates: list[str] = []
        for end in range(1, len(lines) + 1):
            candidate = "\n".join(lines[:end]).strip()
            if candidate:
                candidates.append(candidate)

        extraction["candidate_count"] = len(candidates)
        extraction["first_candidate_preview"] = (
            self._summarize_text(candidates[0], 80) if candidates else ""
        )
        return candidates, extraction

    def _run_candidate_with_timeout(self, sat_code: str, candidate: str) -> tuple[bool, str]:
        ctx = mp.get_context("fork")
        queue = ctx.Queue()
        proc = ctx.Process(
            target=_sandbox_worker,
            args=({"sat_code": sat_code, "candidate": candidate}, queue),
        )
        proc.start()
        proc.join(timeout=self.exec_timeout_seconds)

        if proc.is_alive():
            proc.terminate()
            proc.join()
            return False, f"timeout>{self.exec_timeout_seconds:.2f}s"

        try:
            result = queue.get_nowait()
        except Exception:
            return False, "no_result_from_subprocess"

        if not result.get("ok", False):
            reason = result.get("reason", "unknown_error")
            return False, f"subprocess_error:{reason}"

        if bool(result.get("result", False)):
            return True, "ok"

        return False, "sat_returned_false"

    def _extract_candidate_metadata(self, candidate: str) -> dict:
        try:
            tree = ast.parse(candidate)
        except SyntaxError as exc:
            return {
                "ast_parse_ok": False,
                "parse_error": exc.msg,
                "sol_arg_count": None,
                "redefines_sat": None,
            }

        sat_defs = [
            node
            for node in ast.walk(tree)
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            and node.name == "sat"
        ]
        sol_defs = [
            node
            for node in tree.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            and node.name == "sol"
        ]

        sol_arg_count = None
        if len(sol_defs) == 1:
            sol_arg_count = len(sol_defs[0].args.args)

        return {
            "ast_parse_ok": True,
            "parse_error": None,
            "sol_arg_count": sol_arg_count,
            "redefines_sat": bool(sat_defs),
            "top_level_sol_defs": len(sol_defs),
        }

    def _attempt_output_dir(
        self,
        problem_id: str,
        difficulty: str,
        variant_num: int,
    ) -> Path:
        return self.run_dir / problem_id / f"{difficulty}_{variant_num}"

    def _next_attempt_num(
        self,
        problem_id: str,
        difficulty: str,
        variant_num: int,
    ) -> int:
        attempt_dir = self._attempt_output_dir(problem_id, difficulty, variant_num)
        attempt_dir.mkdir(parents=True, exist_ok=True)

        existing = []
        for child in attempt_dir.iterdir():
            if child.suffix not in {".txt", ".py", ".json"}:
                continue
            stem = child.stem
            if stem.isdigit():
                existing.append(int(stem))
        return (max(existing) + 1) if existing else 1

    def _write_attempt_artifacts(
        self,
        problem_id: str,
        difficulty: str,
        variant_num: int,
        sat_code: str,
        raw_completion: str,
        parsed_candidate: str | None,
        metadata: dict,
    ):
        attempt_num = self._next_attempt_num(problem_id, difficulty, variant_num)
        base = self._attempt_output_dir(problem_id, difficulty, variant_num)

        txt_path = base / f"{attempt_num}.txt"
        py_path = base / f"{attempt_num}.py"
        json_path = base / f"{attempt_num}.json"

        txt_path.write_text(raw_completion, encoding="utf-8")

        sol_source = parsed_candidate
        if not sol_source:
            sol_source = 'def sol():\n    raise RuntimeError("No parseable sol() extracted")\n'

        py_text = f"""{sat_code}

{sol_source}

if __name__ == "__main__":
    assert sat(sol())
"""
        py_path.write_text(py_text, encoding="utf-8")

        json_payload = dict(metadata)
        json_payload.update(
            {
                "problem_id": problem_id,
                "difficulty": difficulty,
                "variant_num": variant_num,
                "attempt_num": attempt_num,
                "created_at": utc_now_iso(),
                "reward_std": float(json_payload.get("reward_std", 0.0)),
            }
        )
        json_path.write_text(
            json.dumps(json_payload, indent=2, sort_keys=True),
            encoding="utf-8",
        )

    def _evaluate_completion_against_sat(
        self,
        sat_code: str,
        completion_text: str,
    ) -> tuple[float, str, str | None]:
        raw_summary = self._summarize_text(completion_text, 120)
        completion_text, fmt_penalty = self._strip_code_fences(completion_text)
        candidates, extraction = self._candidate_prefixes(completion_text)

        parse_mode = (
            f"fence={extraction.get('fence_type','none')},"
            f"preamble={int(bool(extraction.get('had_preamble', False)))},"
            f"found_sol={int(bool(extraction.get('found_def_sol', False)))},"
            f"candidates={extraction.get('candidate_count', 0)}"
        )

        if not candidates:
            return (
                0.0,
                f"reason=no_def_sol|parse={parse_mode}|preview={raw_summary}",
                None,
            )

        last_reason = "no_candidate_succeeded"
        last_candidate = None
        candidates_checked = 0

        for idx, candidate in enumerate(candidates, start=1):
            last_candidate = candidate
            candidates_checked += 1

            try:
                tree = ast.parse(candidate)
            except SyntaxError as exc:
                last_reason = f"ast_syntax_error:{exc.msg}"
                continue

            sat_defs = [
                node
                for node in ast.walk(tree)
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                and node.name == "sat"
            ]
            if sat_defs:
                last_reason = "redefines_sat"
                continue

            sol_defs = [
                node
                for node in tree.body
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                and node.name == "sol"
            ]
            if len(sol_defs) != 1:
                last_reason = f"top_level_sol_defs:{len(sol_defs)}"
                continue

            if len(sol_defs[0].args.args) != 0:
                last_reason = f"sol_has_args:{len(sol_defs[0].args.args)}"
                continue

            try:
                result, reason = self._run_candidate_with_timeout(sat_code, candidate)
            except Exception as exc:
                last_reason = f"sandbox_exception:{type(exc).__name__}:{exc}"
                continue

            if result:
                diag = (
                    f"reason=ok|parse={parse_mode}|candidate={idx}/{len(candidates)}"
                    f"|fmt_penalty={fmt_penalty:.2f}|preview={self._summarize_text(candidate, 120)}"
                )
                return max(0.0, 1.0 - fmt_penalty), diag, candidate

            last_reason = reason

        diag = (
            f"reason={last_reason}|parse={parse_mode}|checked={candidates_checked}/{len(candidates)}"
            f"|preview={raw_summary}"
        )
        return 0.0, diag, last_candidate

    def _reward_func(self, prompts, completions, **kwargs):
        rewards = []
        sat_codes = kwargs.get("sat_code", [])
        problem_ids = kwargs.get("problem_id", [])
        difficulties = kwargs.get("difficulty", [])
        variant_nums = kwargs.get("variant_num", [])

        for idx, completion in enumerate(completions):
            sat_code = sat_codes[idx] if idx < len(sat_codes) else ""
            problem_id = problem_ids[idx] if idx < len(problem_ids) else "unknown_problem"
            difficulty = difficulties[idx] if idx < len(difficulties) else "unknown"
            variant_num = int(variant_nums[idx]) if idx < len(variant_nums) else -1

            if isinstance(completion, list) and len(completion) > 0:
                completion_text = completion[-1].get("content", "").strip()
            else:
                completion_text = str(completion).strip()

            diag = "reason=unknown"
            parsed_candidate = None
            try:
                reward, diag, parsed_candidate = self._evaluate_completion_against_sat(
                    sat_code,
                    completion_text,
                )
            except Exception as exc:
                diag = f"reason=reward_crash:{type(exc).__name__}:{exc}"
                self._warn(
                    f"Reward evaluation crashed for sample {idx}: {type(exc).__name__}: {exc}"
                )
                if self.debug:
                    traceback.print_exc()
                    self._pretty_debug_block("crashing completion", completion_text)
                    self._pretty_debug_block("crashing sat_code", sat_code)
                reward = 0.0

            metadata = {
                "diagnostic": diag,
                "reward": float(reward),
                "reward_std": 0.0,
                "candidate_metadata": self._extract_candidate_metadata(parsed_candidate)
                if parsed_candidate
                else {
                    "ast_parse_ok": False,
                    "parse_error": "no_candidate",
                    "sol_arg_count": None,
                    "redefines_sat": None,
                },
            }
            self._write_attempt_artifacts(
                problem_id=problem_id,
                difficulty=difficulty,
                variant_num=variant_num,
                sat_code=sat_code,
                raw_completion=completion_text,
                parsed_candidate=parsed_candidate,
                metadata=metadata,
            )

            if reward == 0.0:
                print(f"Reward=0 | {diag}")

            if self.debug:
                self._pretty_debug_block("completion", completion_text)
                print(f"[reward] reward={reward:.2f} | {diag}")

            rewards.append(reward)

        return rewards

    def _tokenize_prompt(self, prompt_representation):
        if self.has_native_chat_template:
            return self.tokenizer.apply_chat_template(
                prompt_representation,
                tokenize=True,
                add_generation_prompt=True,
                return_tensors="pt",
                return_dict=True,
            ).to(self.model.device)

        return self.tokenizer(
            prompt_representation,
            return_tensors="pt",
        ).to(self.model.device)

    def _prepare_problem_dataset(self, dataset: dict | Dataset):
        if isinstance(dataset, Dataset):
            dataset = {"hard": list(dataset)}
        elif not isinstance(dataset, dict):
            raise TypeError("dataset must be a dict or Dataset")

        train_dataset: dict[str, list[dict[str, Any]]] = {}
        for difficulty, problems in dataset.items():
            train_dataset[difficulty] = []
            for idx, problem in enumerate(problems):
                prompt_text = problem["prompt"]
                messages = self._build_prompt_representation(prompt_text)
                train_dataset[difficulty].append(
                    {
                        "prompt": messages,
                        "sat_code": prompt_text,
                        "problem_id": problem.get("problem_id", f"unknown_problem_{idx}"),
                        "difficulty": difficulty,
                        "variant_num": int(problem.get("variant_num", idx)),
                        "source_name": problem.get("source_name", ""),
                        "notes": problem.get("notes", ""),
                    }
                )
        return train_dataset

    def _attach_problem_id_to_tree(self, problem_id: str, tree: dict) -> dict:
        attached = {}
        for difficulty, problems in tree.items():
            attached[difficulty] = []
            for idx, problem in enumerate(problems):
                copy = dict(problem)
                copy.setdefault("problem_id", problem_id)
                copy.setdefault("variant_num", idx)
                attached[difficulty].append(copy)
        return attached

    def _snapshot_trainable_state(self) -> dict[str, torch.Tensor]:
        model_for_snapshot = self.trainer.model if self.trainer is not None else self.model
        return {
            name: param.detach().float().cpu().clone()
            for name, param in model_for_snapshot.named_parameters()
            if param.requires_grad
        }

    def _summarize_weight_changes(
        self,
        before: dict[str, torch.Tensor],
        after: dict[str, torch.Tensor],
    ) -> tuple[int, int, float, float]:
        total_tensors = 0
        changed_tensors = 0
        total_elements = 0
        changed_elements = 0

        for name, before_tensor in before.items():
            after_tensor = after.get(name)
            if after_tensor is None:
                continue

            total_tensors += 1
            diff_mask = before_tensor.ne(after_tensor)
            num_changed = int(diff_mask.sum().item())
            num_total = before_tensor.numel()

            total_elements += num_total
            changed_elements += num_changed

            if num_changed > 0:
                changed_tensors += 1

        pct_changed_tensors = (
            100.0 * changed_tensors / total_tensors if total_tensors > 0 else 0.0
        )
        pct_changed_elements = (
            100.0 * changed_elements / total_elements if total_elements > 0 else 0.0
        )

        return changed_tensors, total_tensors, pct_changed_tensors, pct_changed_elements

    def _get_default_peft_config(self):
        return LoraConfig(
            r=16,
            lora_alpha=32,
            lora_dropout=0.05,
            bias="none",
            task_type="CAUSAL_LM",
            target_modules=[
                "q_proj",
                "k_proj",
                "v_proj",
                "o_proj",
                "gate_proj",
                "up_proj",
                "down_proj",
            ],
        )

    def _ensure_peft_model(self, peft_config: LoraConfig | None = None):
        if self._peft_initialized or isinstance(self.model, PeftModel):
            self._peft_initialized = True
            return

        if peft_config is None:
            peft_config = self._get_default_peft_config()

        self.model = get_peft_model(self.model, peft_config)
        self.model.train()
        self._peft_initialized = True

        trainable = 0
        total = 0
        for _, param in self.model.named_parameters():
            total += param.numel()
            if param.requires_grad:
                trainable += param.numel()

        pct = 100.0 * trainable / total if total > 0 else 0.0
        print(f"Initialized LoRA adapter | trainable params: {trainable}/{total} ({pct:.4f}%)")

    def load_adapter_checkpoint(self, checkpoint_dir: Path):
        checkpoint_dir = Path(checkpoint_dir)
        if not checkpoint_dir.exists():
            raise FileNotFoundError(f"Checkpoint directory does not exist: {checkpoint_dir}")

        if isinstance(self.model, PeftModel):
            self.model.load_adapter(str(checkpoint_dir), adapter_name="resume_adapter")
            self.model.set_adapter("resume_adapter")
        else:
            self.model = PeftModel.from_pretrained(
                self.model,
                str(checkpoint_dir),
                is_trainable=True,
            )
        self.model.train()
        self._peft_initialized = True
        self.trainer = None

    def _create_trainer(self, train_dataset: Dataset, training_args: GRPOConfig):
        trainer = GRPOTrainer(
            model=self.model,
            args=training_args,
            train_dataset=train_dataset,
            reward_funcs=self._reward_func,
            processing_class=self.tokenizer,
        )
        trainer.remove_callback(PrinterCallback)
        trainer.remove_callback(ProgressCallback)
        trainer.add_callback(RewardProgressCallback())
        return trainer

    def train_on_tree(
        self,
        problem_id: str,
        tree: dict,
        max_steps: int = 20,
        target_accuracy: float = 0.8,
        learning_rate: float = 5e-6,
        group_size: int = 4,
        problem_artifacts_dir: Path | None = None,
        peft_config: LoraConfig | None = None,
    ):
        self._ensure_peft_model(peft_config)
        tree = self._attach_problem_id_to_tree(problem_id, tree)
        prepared = self._prepare_problem_dataset(tree)

        for difficulty in self.difficulty_order:
            if difficulty not in prepared:
                continue

            problems = prepared[difficulty]
            if not problems:
                continue

            print(f"\n{'=' * 50}")
            print(f"Training on {difficulty} ({len(problems)} problems)")
            print(f"{'=' * 50}")

            train_dataset = Dataset.from_list(problems)

            training_args = GRPOConfig(
                output_dir=str(self.run_dir / "artifacts" / "trainer_tmp"),
                per_device_train_batch_size=1,
                gradient_accumulation_steps=4,
                learning_rate=learning_rate,
                max_steps=max_steps,
                logging_steps=1,
                num_generations=group_size,
                max_completion_length=256,
                temperature=0.8,
                top_p=0.95,
                fp16=False,
                bf16=True,
            )

            before_state = self._snapshot_trainable_state()

            # Fresh trainer each phase; same already-wrapped LoRA model.
            # Reusing a GRPOTrainer after .train() can leave Accelerate state invalid.
            self.trainer = self._create_trainer(train_dataset, training_args)
            self.model = self.trainer.model

            self.trainer.train()
            self.model = self.trainer.model

            after_state = self._snapshot_trainable_state()
            (
                changed_tensors,
                total_tensors,
                pct_changed_tensors,
                pct_changed_elements,
            ) = self._summarize_weight_changes(before_state, after_state)

            print(
                "Weight change summary: "
                f"{changed_tensors}/{total_tensors} trainable tensors changed "
                f"({pct_changed_tensors:.2f}% of tensors, {pct_changed_elements:.6f}% of elements)"
            )

            accuracy = self._evaluate_accuracy(
                Dataset.from_list(problems),
                num_samples=1,
                max_new_tokens=256,
                do_sample=False,
            )
            print(f"\nAccuracy on {difficulty}: {accuracy:.2%}")

            if accuracy >= target_accuracy:
                print(f"Target accuracy {target_accuracy:.0%} reached for {difficulty}")
            else:
                print(f"Warning: Target accuracy {target_accuracy:.0%} not reached for {difficulty}")

        if problem_artifacts_dir is not None:
            problem_artifacts_dir.mkdir(parents=True, exist_ok=True)

    def evaluate_performance(
        self,
        dataset: Dataset,
        num_samples: int = 1,
        max_new_tokens: int = 256,
        do_sample: bool = False,
    ) -> dict:
        prepared = self._prepare_problem_dataset(dataset)
        out = {}

        for difficulty in self.difficulty_order:
            if difficulty not in prepared:
                continue

            problems = prepared[difficulty]
            if not problems:
                continue

            out[difficulty] = self._evaluate_accuracy(
                Dataset.from_list(problems),
                num_samples=num_samples,
                max_new_tokens=max_new_tokens,
                do_sample=do_sample,
            )
            print(f"Problem group {difficulty}: {out[difficulty] * 100:.2f}% accuracy pass@1")

        return out

    def _evaluate_accuracy(
        self,
        dataset: Dataset,
        num_samples: int = 1,
        max_new_tokens: int = 256,
        do_sample: bool = False,
    ) -> float:
        self.model.eval()
        correct = 0.0
        total = 0

        for problem in tqdm(list(dataset), desc="Evaluating", unit="problem"):
            prompt_representation = problem["prompt"]
            inputs = self._tokenize_prompt(prompt_representation)

            for _ in range(num_samples):
                gen_kwargs = dict(
                    **inputs,
                    do_sample=do_sample,
                    max_new_tokens=max_new_tokens,
                    pad_token_id=self.tokenizer.eos_token_id,
                )
                if do_sample:
                    gen_kwargs["temperature"] = 0.8
                    gen_kwargs["top_p"] = 0.95

                with torch.no_grad():
                    output_ids = self.model.generate(**gen_kwargs)

                completion_text = self._decode_generated_completion(inputs, output_ids)

                if self.debug:
                    self._pretty_debug_block("eval completion", completion_text)

                reward = self._reward_func(
                    [prompt_representation],
                    [completion_text],
                    sat_code=[problem["sat_code"]],
                    problem_id=[problem["problem_id"]],
                    difficulty=[problem["difficulty"]],
                    variant_num=[problem["variant_num"]],
                )[0]

                correct += reward
                total += 1

        return correct / total if total > 0 else 0.0

    def save_problem_checkpoint(self, problem_id: str) -> Path:
        checkpoint_dir = self.run_dir / problem_id / "artifacts" / "checkpoint"
        checkpoint_dir.mkdir(parents=True, exist_ok=True)

        model_to_save = self.trainer.model if self.trainer is not None else self.model
        model_to_save.save_pretrained(str(checkpoint_dir))
        self.tokenizer.save_pretrained(str(checkpoint_dir))
        return checkpoint_dir

    def save_final_checkpoint(self) -> Path:
        final_dir = self.run_dir / "artifacts" / "final"
        final_dir.mkdir(parents=True, exist_ok=True)

        model_to_save = self.trainer.model if self.trainer is not None else self.model
        model_to_save.save_pretrained(str(final_dir))
        self.tokenizer.save_pretrained(str(final_dir))
        return final_dir

    @torch.no_grad()
    def generate(
        self,
        prompt: str,
        max_new_tokens: int = 256,
        do_sample: bool = True,
    ) -> str:
        self.model.eval()

        prompt_representation = self._build_prompt_representation(prompt)
        inputs = self._tokenize_prompt(prompt_representation)

        gen_kwargs = dict(
            **inputs,
            do_sample=do_sample,
            max_new_tokens=max_new_tokens,
            pad_token_id=self.tokenizer.eos_token_id,
        )
        if do_sample:
            gen_kwargs["temperature"] = 0.8
            gen_kwargs["top_p"] = 0.95

        output_ids = self.model.generate(**gen_kwargs)
        return self._decode_generated_completion(inputs, output_ids)
