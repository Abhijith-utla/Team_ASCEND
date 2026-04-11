#!/usr/bin/env python3

import ast
import json
import re
from datetime import datetime, timezone
from pathlib import Path

import torch


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def make_variant_prompt(sat_code: str, notes: str) -> str:
    return f"""You are generating simpler Python Programming Puzzles.

A puzzle is a Python function named sat() that takes an answer and returns True exactly when the answer is correct.

Original puzzle:
{sat_code}

Description:
{notes}

Generate exactly 3 simpler variants that test the same core concept.

Requirements:
- Each variant must be a complete, syntactically valid Python function named sat
- Do not include explanations
- Do not include comments outside the function
- Do not include markdown code fences
- Output only the three labeled variants below

Required output format:

VARIANT1:
def sat(...):
    ...

VARIANT2:
def sat(...):
    ...

VARIANT3:
def sat(...):
    ...
"""


def _write_text(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_json(path: Path, payload: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def _variant_logs_dir(run_dir: Path, problem_id: str) -> Path:
    return run_dir / problem_id / "artifacts" / "variant_generations"


def _save_variant_generation_artifacts(
    run_dir: Path,
    problem_id: str,
    stage: str,
    source_variant_num: int,
    attempt_num: int,
    raw_output: str,
    parsed_variants: list[dict],
):
    base = _variant_logs_dir(run_dir, problem_id) / f"{stage}_{source_variant_num}"
    _write_text(base / f"{attempt_num}.txt", raw_output)
    _write_json(
        base / f"{attempt_num}.json",
        {
            "problem_id": problem_id,
            "stage": stage,
            "source_variant_num": source_variant_num,
            "attempt_num": attempt_num,
            "created_at": utc_now_iso(),
            "parsed_variant_count": len(parsed_variants),
            "parsed_variant_nums": [v.get("variant_num") for v in parsed_variants],
        },
    )

    for variant in parsed_variants:
        variant_num = variant.get("variant_num", -1)
        sat_code = variant["prompt"]
        py_text = f"""{sat_code}

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
"""
        _write_text(base / f"{attempt_num}_parsed_variant_{variant_num}.py", py_text)


def generate_variants(
    model,
    tokenizer,
    has_native_chat_template: bool,
    sat_code: str,
    notes: str,
    max_new_tokens: int = 800,
) -> str:
    prompt = make_variant_prompt(sat_code, notes)

    if has_native_chat_template:
        messages = [{"role": "user", "content": prompt}]
        inputs = tokenizer.apply_chat_template(
            messages,
            tokenize=True,
            add_generation_prompt=True,
            return_tensors="pt",
            return_dict=True,
        ).to(model.device)
    else:
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            temperature=0.8,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id,
        )

    generated_ids = output_ids[0][inputs["input_ids"].shape[1] :]
    return tokenizer.decode(generated_ids, skip_special_tokens=True)


def parse_variants(raw_output: str) -> list[dict]:
    def strip_fences(text: str) -> str:
        text = text.strip()
        text = re.sub(r"^```(?:python)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
        return text.strip()

    def extract_sat_prefix(block: str) -> str | None:
        block = strip_fences(block)

        start = block.find("def sat(")
        if start == -1:
            return None

        block = block[start:].strip()
        lines = block.splitlines()

        best = None
        for end in range(1, len(lines) + 1):
            candidate = "\n".join(lines[:end]).strip()
            if not candidate:
                continue

            try:
                tree = ast.parse(candidate)
            except SyntaxError:
                continue

            has_sat = any(
                isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                and node.name == "sat"
                for node in tree.body
            )
            if has_sat:
                best = candidate

        return best

    text = strip_fences(raw_output)

    pattern = re.compile(
        r"VARIANT([123]):\s*(.*?)(?=(?:\nVARIANT[123]:)|\Z)",
        re.DOTALL | re.IGNORECASE,
    )

    variants: list[dict] = []
    seen = set()

    for label, block in pattern.findall(text):
        sat_code = extract_sat_prefix(block)
        if sat_code is None:
            continue

        normalized = sat_code.strip()
        if normalized in seen:
            continue

        seen.add(normalized)
        variants.append(
            {
                "prompt": normalized,
                "variant_num": int(label),
            }
        )

    return variants


def generate_variant_tree(
    model,
    tokenizer,
    has_native_chat_template: bool,
    sat_code: str,
    notes: str,
    problem_id: str,
    run_dir: Path,
    max_new_tokens: int = 800,
    max_retries: int = 3,
) -> dict:
    out = {
        "hard": [
            {
                "prompt": sat_code,
                "variant_num": 0,
            }
        ],
        "medium": [],
        "easy": [],
    }

    for attempt in range(1, max_retries + 1):
        raw = generate_variants(
            model=model,
            tokenizer=tokenizer,
            has_native_chat_template=has_native_chat_template,
            sat_code=sat_code,
            notes=notes,
            max_new_tokens=max_new_tokens,
        )
        parsed = parse_variants(raw)
        _save_variant_generation_artifacts(
            run_dir=run_dir,
            problem_id=problem_id,
            stage="medium",
            source_variant_num=0,
            attempt_num=attempt,
            raw_output=raw,
            parsed_variants=parsed,
        )

        if len(parsed) == 3:
            out["medium"] = [
                {"prompt": v["prompt"], "variant_num": v["variant_num"]} for v in parsed
            ]
            break

        print(f"[medium] attempt {attempt}/{max_retries} failed: parsed {len(parsed)} variants")

    easy_counter = 1
    for medium_variant in out["medium"]:
        medium_variant_num = medium_variant["variant_num"]
        accepted = None

        for attempt in range(1, max_retries + 1):
            raw = generate_variants(
                model=model,
                tokenizer=tokenizer,
                has_native_chat_template=has_native_chat_template,
                sat_code=medium_variant["prompt"],
                notes="No description available",
                max_new_tokens=max_new_tokens,
            )
            parsed = parse_variants(raw)
            _save_variant_generation_artifacts(
                run_dir=run_dir,
                problem_id=problem_id,
                stage="easy_from_medium",
                source_variant_num=medium_variant_num,
                attempt_num=attempt,
                raw_output=raw,
                parsed_variants=parsed,
            )

            if len(parsed) == 3:
                accepted = parsed
                break

            print(
                f"[easy from medium {medium_variant_num}] attempt {attempt}/{max_retries} "
                f"failed: parsed {len(parsed)} variants"
            )

        if accepted is not None:
            for parsed_variant in accepted:
                out["easy"].append(
                    {
                        "prompt": parsed_variant["prompt"],
                        "variant_num": easy_counter,
                    }
                )
                easy_counter += 1

    return out
