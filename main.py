#!/usr/bin/env python3

import json
import os

import torch
from datasets import Dataset

import ladder_optimizer_v2 as lo


PUZZLES_PATH = "PythonProgrammingPuzzles/puzzles/puzzles.json"
MODEL_ID = "deepseek-ai/deepseek-coder-1.3b-instruct"


def load_puzzles(path: str = PUZZLES_PATH) -> list[dict]:
    if not os.path.exists(path):
        raise FileNotFoundError(f"puzzles.json not found at: {path}")

    with open(path, "r", encoding="utf-8") as f:
        puzzles = json.load(f)

    if not puzzles:
        raise ValueError("No puzzles found")

    return puzzles


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
    import ast
    import re

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

    for _, block in pattern.findall(text):
        sat_code = extract_sat_prefix(block)
        if sat_code is None:
            continue

        normalized = sat_code.strip()
        if normalized in seen:
            continue

        seen.add(normalized)
        variants.append({"prompt": normalized})

    return variants


def generate_variant_tree(
    model,
    tokenizer,
    has_native_chat_template: bool,
    sat_code: str,
    notes: str,
    max_new_tokens: int = 800,
    max_retries: int = 3,
    debug_print_raw: bool = True,
) -> dict:
    out = {
        "hard": [{"prompt": sat_code}],
        "medium": [],
        "easy": [],
    }

    for attempt in range(max_retries):
        raw = generate_variants(
            model=model,
            tokenizer=tokenizer,
            has_native_chat_template=has_native_chat_template,
            sat_code=sat_code,
            notes=notes,
            max_new_tokens=max_new_tokens,
        )

        if debug_print_raw:
            print("\n--- RAW MEDIUM GENERATION ---")
            print(raw)
            print("--- END RAW MEDIUM GENERATION ---\n")

        variants = parse_variants(raw)
        if len(variants) == 3:
            out["medium"] = variants
            break

        print(
            f"[medium] attempt {attempt + 1}/{max_retries} failed: parsed {len(variants)} variants"
        )

    for idx, subproblem in enumerate(out["medium"]):
        accepted = None
        for attempt in range(max_retries):
            raw = generate_variants(
                model=model,
                tokenizer=tokenizer,
                has_native_chat_template=has_native_chat_template,
                sat_code=subproblem["prompt"],
                notes="No description available",
                max_new_tokens=max_new_tokens,
            )

            if debug_print_raw:
                print(f"\n--- RAW EASY GENERATION FROM MEDIUM {idx} ---")
                print(raw)
                print(f"--- END RAW EASY GENERATION FROM MEDIUM {idx} ---\n")

            variants = parse_variants(raw)
            if len(variants) == 3:
                accepted = variants
                break

            print(
                f"[easy from medium {idx}] attempt {attempt + 1}/{max_retries} failed: "
                f"parsed {len(variants)} variants"
            )

        if accepted is not None:
            out["easy"].extend(accepted)

    return out


def main():
    puzzles = load_puzzles()

    print(f"Total puzzles: {len(puzzles)}")
    print("Keys in each puzzle:", puzzles[0].keys())
    print("\n--- Example puzzle ---")
    print(puzzles[0])

    model, tokenizer, has_native_chat_template = lo.load_default_model(MODEL_ID)
    print("Model loaded!")
    print(f"Model ID: {MODEL_ID}")
    print(f"Using native chat template: {has_native_chat_template}")

    print("Beginning train step")

    base_dataset = [{"prompt": puzzle["sat"]} for puzzle in puzzles]
    print(f"Discovered {len(base_dataset)} base problems")

    print("Restricting initial train step to 10 problems for debugging PLEASE REMOVE LATER")
    base_dataset = base_dataset[:10]

    eval_trainer = lo.LadderOptimizer(
        Dataset.from_list(base_dataset),
        model,
        tokenizer,
        debug=False,
        has_native_chat_template=has_native_chat_template,
    )

    print("\n=== Evaluate Pre-train accuracy ===")
    eval_trainer.evaluate_performance()

    print("\n=== Beginning Train Loop ===")
    for i, problem in enumerate(base_dataset):
        sat_code = problem["prompt"]
        print(f"    Starting problem {i + 1} of {len(base_dataset)}...")

        print("    Generating variant tree... ", end="")
        tree = generate_variant_tree(
            model,
            tokenizer,
            has_native_chat_template,
            sat_code,
            "No description available",
            debug_print_raw=False,
        )
        print("Done!")

        print("    --- Variant Tree Summary (filtering disabled) ---")
        print(f"        hard:   {len(tree['hard'])}")
        print(f"        medium: {len(tree['medium'])}")
        print(f"        easy:   {len(tree['easy'])}")
        print()

        print("    Creating LadderOptimizer... ", end="")
        opt = lo.LadderOptimizer(
            tree,
            model,
            tokenizer,
            debug=False,
            has_native_chat_template=has_native_chat_template,
        )
        print("Done!")

        print("\n    --- Begin Training --- ")
        opt.train(
            max_steps=20,
            target_accuracy=0.8,
            learning_rate=5e-6,
            group_size=4,
        )

        model = opt.model

    print("\n=== Evaluate Post-train accuracy ===")
    post_eval_trainer = lo.LadderOptimizer(
        Dataset.from_list(base_dataset),
        model,
        tokenizer,
        debug=False,
        has_native_chat_template=has_native_chat_template,
    )
    post_eval_trainer.evaluate_performance()


if __name__ == "__main__":
    main()
