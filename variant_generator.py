import torch
#!/usr/bin/env python3
# Converted from variant_generator.ipynb
import os
import json
from datasets import Dataset

assert os.path.exists("PythonProgrammingPuzzles/puzzles/puzzles.json"), (
    "puzzles.json not found"
)

with open("PythonProgrammingPuzzles/puzzles/puzzles.json", "r") as f:
    puzzles = json.load(f)

print(f"Total puzzles: {len(puzzles)}")
print("Keys in each puzzle:", puzzles[0].keys())
print("\n--- Example puzzle ---")
print(puzzles[0])

# # --- Code cell 5 ---
# from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
# import torch
#
# model_name = "Qwen/Qwen2.5-Coder-7B-Instruct"
#
# bnb_config = BitsAndBytesConfig(
#     load_in_4bit=True,
#     bnb_4bit_compute_dtype=torch.float16,
# )
#
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(
#     model_name,
#     quantization_config=bnb_config,
#     device_map="auto",
# )
#
import ladder_optimizer as lo

model, tokenizer = lo.load_default_model("bigcode/starcoder2-3b")

print("Model loaded!")


# --- Code cell 6 ---
def make_variant_prompt(sat_code: str, notes: str) -> str:
    return f"""You are a programming puzzle designer working with Python Programming Puzzles (P3).

Each P3 puzzle is a Python function called sat() that takes an answer as input and returns True if the answer is correct. The solver's job is to find an input that makes sat() return True.

Here is an original puzzle:
{sat_code}

Description: {notes}

Generate exactly 3 variants/subproblems of this puzzle at a roughly 50% difficulty to the original.

These problems should test the same core category of problems, but should have a simpler logic, fewer3 constraints, or a better structural hint. They should be considerably simpler than the original. 

For example, given a problem which wants a derangement of a list, a simpler problem could be a problem which simply wants a list that has a given length and each element within certain bounds.

Rules for all variants:
1. Must be a valid sat() function in the same format
2. Must test the same core algorithmic concept
3. Must be syntactically valid Python
4. Must still require actual logic to solve

Output in exactly this format, no extra commentary:
VARIANT1:
<sat function here>

VARIANT2:
<sat function here>

VARIANT3:
<sat function here>
"""


def generate_variants(
    model, sat_code: str, notes: str, max_new_tokens: int = 800
) -> str:
    prompt = make_variant_prompt(sat_code, notes)
    messages = [{"role": "user", "content": prompt}]

    text = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

    inputs = tokenizer([text], return_tensors="pt").to(model.device)

    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            temperature=0.8,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id,
        )

    generated = output_ids[0][inputs["input_ids"].shape[1] :]
    return tokenizer.decode(generated, skip_special_tokens=True)


# --- Code cell 7 ---
import re


def parse_variants(raw_output: str) -> list[dict]:
    variants = []

    # Strip markdown code fences before matching
    clean_output = re.sub(r"```python\n|```", "", raw_output)

    pattern = r"(VARIANT1|VARIANT2|VARIANT3):\s*(def sat[\s\S]*?)(?=(?:VARIANT1|VARIANT2|VARIANT3):|$)"
    matches = re.findall(pattern, clean_output, re.IGNORECASE)

    for label, code in matches:
        level = label.lower()
        variants.append({"prompt": code.strip()})

    return variants


def process_puzzle(puzzle: dict) -> list[dict]:
    sat_code = puzzle["sat"]
    notes = puzzle.get("notes", "No description available")
    name = puzzle["name"]

    raw_output = generate_variants(model, sat_code, notes)
    return parse_variants(raw_output)


def generate_variant_tree(
    model, sat_code: str, notes: str, max_new_tokens: int = 800
) -> dict:
    out = {"hard": [{"prompt": sat_code}], "medium": [], "easy": []}

    MAX_RETRIES = 3

    for attempt in range(MAX_RETRIES):
        vars = parse_variants(generate_variants(model, sat_code, notes))
        if vars and len(vars) == 3:
            out["medium"] = vars
        else:
            print(f"Failed, continuing to attempt {attempt} on medium")

    for subproblem in out["medium"]:
        for attempt in range(MAX_RETRIES):
            vars = parse_variants(
                generate_variants(
                    model, subproblem["prompt"], "No description available"
                )
            )
            if vars and len(vars) == 3:
                out["easy"].extend(vars)
            else:
                print(f"Failed, continuing to attempt {attempt} on easy")

    return out


# --- Code cell 8 ---
print("Beginning train step")

base_dataset = [{"prompt": puzzle["sat"]} for puzzle in puzzles]

print(f"Discovered {len(base_dataset)} base problems")

print("Restricting initial train step to 10 problems for debugging PLEASE REMOVE LATER")
base_dataset = base_dataset[:10]

eval_trainer = lo.LadderOptimizer(Dataset.from_list(base_dataset), model, tokenizer)

print("\n=== Evaluate Pre-train accuracy ===")

eval_trainer.evaluate_performance()

print("\n=== Beginning Train Loop ===")
for i, problem in enumerate(base_dataset):
    sat_code = problem["prompt"]
    print(f"    Starting problem {i} of {len(base_dataset)}...")
    print("    Generating variant tree... ", end="")
    tree = generate_variant_tree(model, sat_code, "No description available")
    print("Done!")

    print("    Creating LadderOptimizer... ", end="")
    opt = lo.LadderOptimizer(tree, model, tokenizer)
    print("end!")

    print("\n   --- Begin Training --- ")
    opt.train(max_steps=20, target_accuracy=0.8, learning_rate=5e-6, group_size=4)

    model = opt.model

print("\n=== Evaluate Post-train accuracy ===")

post_eval_trainer = lo.LadderOptimizer(
    Dataset.from_list(base_dataset), model, tokenizer
)

post_eval_trainer.evaluate_performance()


# all_results = []
#
# MAX_RETRIES = 3
#
# for i, puzzle in enumerate(puzzles[:10]):
#     print(f"Processing {i+1}/10: {puzzle['name']}")
#
#     entry = None
#     for attempt in range(MAX_RETRIES):
#         entry = process_puzzle(puzzle)
#         missing = [lvl for lvl in ["easy", "medium", "hard"] if not entry[lvl]]
#         if not missing:
#             print(f"  All 3 tiers parsed successfully")
#             break
#         print(f"  Attempt {attempt+1} failed: missing {missing}, retrying...")
#
#     if missing:
#         print(f"  GIVING UP on {puzzle['name']} after {MAX_RETRIES} attempts, skipping")
#     else:
#         all_results.append(entry)
#
# with open("variants_ladder.json", "w") as f:
#     json.dump(all_results, f, indent=2)
#
# print(f"\nSaved {len(all_results)} complete problems to variants_ladder.json")
#
# # --- Code cell 9 ---
# entry = all_results[0]
# print(f"Problem: {entry['name']}")
# print(f"Notes:   {entry['notes']}")
# print()
# for level in ["easy", "medium", "hard"]:
#     print(f"{level.upper()}:")
#     print(entry[level][0]["prompt"])
#     print("-" * 40)
#
# # --- Code cell 10 ---
# pass
