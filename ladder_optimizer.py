import torch
from datasets import Dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig
from trl import GRPOConfig, GRPOTrainer

SYSTEM_PROMPT = (
    "You are a Python code generator.\n"
    "Define a function sol() such that assert sat(sol()) is True for the given sat() function.\n"
    "Output ONLY the Python function definition for sol() and any necessary import statements.\n"
    "Do NOT wrap your output in markdown code blocks.\n"
    "Do NOT include any explanations, commentary, or text outside of the Python code.\n\n"
)


def load_default_model(model_id: str = "Qwen/Qwen2.5-Coder-3B-Instruct"):
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.float16,
        device_map=None,
        low_cpu_mem_usage=True,
    ).to("cuda")
    model.eval()
    return model, tokenizer


class LadderOptimizer:
    def __init__(self, dataset: dict | Dataset, model, tokenizer):
        if isinstance(dataset, dict):
            self._validate_dataset_dict(dataset)
            self.dataset = dataset
        elif isinstance(dataset, Dataset):
            self.dataset = {"hard": dataset}
        else:
            raise TypeError("dataset must be a dict or Dataset")

        self.model = model
        self.tokenizer = tokenizer
        self.trainer = None
        self.difficulty_order = ["easy", "medium", "hard"]

        # Build conversational prompts (system + user) for training
        self.train_dataset = {}
        for difficulty, problems in self.dataset.items():
            self.train_dataset[difficulty] = []
            for problem in problems:
                messages = [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": problem["prompt"]},
                ]
                self.train_dataset[difficulty].append(
                    {
                        "prompt": messages,
                        "sat_code": problem["prompt"],
                    }
                )

    def _validate_dataset_dict(self, dataset: dict):
        valid_keys = {"easy", "medium", "hard"}
        if not all(k in valid_keys for k in dataset.keys()):
            raise ValueError(f"Dataset dict must have keys from {valid_keys}")

        for difficulty, problems in dataset.items():
            if not isinstance(problems, list):
                raise TypeError(f"dataset['{difficulty}'] must be a list")
            for i, problem in enumerate(problems):
                if not isinstance(problem, dict):
                    raise TypeError(f"dataset['{difficulty}'][{i}] must be a dict")
                if "prompt" not in problem:
                    raise KeyError(f"dataset['{difficulty}'][{i}] missing 'prompt' key")

    def _reward_func(self, prompts, completions, **kwargs):
        rewards = []
        sat_codes = kwargs.get("sat_code", [])

        for i, (prompt, completion) in enumerate(zip(prompts, completions)):
            # Get sat_code from extra dataset field (passed via kwargs)
            sat_code = sat_codes[i] if sat_codes else ""

            # Extract sol content from conversational completion format
            if isinstance(completion, list) and len(completion) > 0:
                sol_code = completion[-1].get("content", "").strip()
            else:
                sol_code = str(completion).strip()

            fmt_penalty = 0.0

            # Strip code fence artifacts
            if sol_code.startswith("```python"):
                sol_code = sol_code[9:].strip()
                fmt_penalty += 0.05
            if sol_code.startswith("```"):
                sol_code = sol_code[3:].strip()
                fmt_penalty += 0.05
            if sol_code.endswith("```"):
                sol_code = sol_code[:-3].strip()
                fmt_penalty += 0.05
            if sol_code.endswith("```"):
                sol_code = sol_code[:-3].strip()
                fmt_penalty += 0.05

            test_string = f"{sat_code}\n\n{sol_code}\n\nassert sat(sol())"

            try:
                print(f"=== Executing Code ===\n{test_string}\n")
                exec(test_string, {}, {})
                rewards.append(1.0 - fmt_penalty)
            except:
                rewards.append(0.0)

        return rewards

    def evaluate_performance(self) -> dict:
        out = {}
        for difficulty in self.difficulty_order:
            if difficulty not in self.train_dataset:
                continue

            problems = self.train_dataset[difficulty]
            if not problems:
                continue

            out[difficulty] = self._evaluate_accuracy(problems)
            print(
                f"Problem group {difficulty}: {out[difficulty] * 100}% accuracy pass@1"
            )

        return out

    def _evaluate_accuracy(self, problems: list[dict], num_samples: int = 4) -> float:
        self.model.eval()
        correct = 0
        total = 0

        for problem in problems:
            messages = problem["prompt"]

            inputs = self.tokenizer.apply_chat_template(
                messages,
                tokenize=True,
                add_generation_prompt=True,
                return_tensors="pt",
                return_dict=True,
            ).to(self.model.device)

            for _ in range(num_samples):
                with torch.no_grad():
                    output = self.model.generate(
                        **inputs,
                        do_sample=True,
                        temperature=0.8,
                        top_p=0.95,
                        max_new_tokens=256,
                        pad_token_id=self.tokenizer.eos_token_id,
                    )

                # Decode with special tokens to find assistant turn boundary
                full_text = self.tokenizer.decode(output[0], skip_special_tokens=False)
                # Find the last assistant turn marker
                marker = "<|im_start|>assistant\n"
                marker_pos = full_text.rfind(marker)
                if marker_pos >= 0:
                    completion = full_text[marker_pos + len(marker):]
                else:
                    completion = full_text

                if completion.endswith("<|im_end|>"):
                    completion = completion[:-1 * len("<|im_end|>")]

                try:
                    reward = self._reward_func(
                        [messages],
                        [completion],
                        sat_code=[problem["sat_code"]],
                    )[0]
                    correct += reward
                except ValueError:
                    pass
                total += 1

        return correct / total if total > 0 else 0.0

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

    def train(
        self,
        max_steps: int = 20,
        target_accuracy: float = 0.8,
        learning_rate: float = 5e-6,
        group_size: int = 4,
        output_dir: str = "grpo_out",
        peft_config: LoraConfig = None,
    ):
        if peft_config is None:
            peft_config = self._get_default_peft_config()

        for difficulty in self.difficulty_order:
            if difficulty not in self.train_dataset:
                continue

            problems = self.train_dataset[difficulty]
            if not problems:
                continue

            print(f"\n{'=' * 50}")
            print(f"Training on {difficulty} ({len(problems)} problems)")
            print(f"{'=' * 50}")

            train_dataset = Dataset.from_list(problems)

            training_args = GRPOConfig(
                output_dir=output_dir,
                per_device_train_batch_size=1,
                gradient_accumulation_steps=4,
                learning_rate=learning_rate,
                max_steps=max_steps,
                logging_steps=1,
                num_generations=group_size,
                max_completion_length=256,
                temperature=0.8,
                top_p=0.95,
                fp16=True,
            )

            self.trainer = GRPOTrainer(
                model=self.model,
                args=training_args,
                train_dataset=train_dataset,
                reward_funcs=self._reward_func,
                processing_class=self.tokenizer,
                peft_config=peft_config,
            )

            self.trainer.train()

            accuracy = self._evaluate_accuracy(problems)
            print(f"\nAccuracy on {difficulty}: {accuracy:.2%}")

            if accuracy >= target_accuracy:
                print(f"Target accuracy {target_accuracy:.0%} reached for {difficulty}")
            else:
                print(
                    f"Warning: Target accuracy {target_accuracy:.0%} not reached for {difficulty}"
                )

        if self.trainer is not None:
            final_path = f"{output_dir}/final"
            self.trainer.save_model(final_path)
            self.tokenizer.save_pretrained(final_path)
            print(f"\nModel saved to {final_path}")

        return self.trainer

    @torch.no_grad()
    def generate(self, prompt: str, max_new_tokens: int = 256) -> str:
        self.model.eval()
        full_prompt = SYSTEM_PROMPT + prompt
        inputs = self.tokenizer(full_prompt, return_tensors="pt").to(self.model.device)

        output = self.model.generate(
            **inputs,
            do_sample=True,
            temperature=0.8,
            top_p=0.95,
            max_new_tokens=max_new_tokens,
            pad_token_id=self.tokenizer.eos_token_id,
        )

        text = self.tokenizer.decode(output[0], skip_special_tokens=True)
        if text.startswith(full_prompt):
            return text[len(full_prompt) :]
        return text
