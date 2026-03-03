import os
import json
import time
import re
import ast
import math
from openai import OpenAI
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()

client = OpenAI(
    base_url="https://api.featherless.ai/v1",
    api_key=os.environ.get("FEATHERLESS_API_KEY"),
)


# -------------------------
# Difficulty quantification
# -------------------------
def difficulty_score(code: str) -> float:
    """
    Rough difficulty score in [0, 100] based on AST complexity.
    Higher = more complex / harder.
    """
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return 100.0  # if invalid code, treat as very hard

    loops = branches = bool_ops = calls = comps = 0
    total_nodes = 0
    max_depth = 0

    def visit(node, depth=0):
        nonlocal loops, branches, bool_ops, calls, comps, total_nodes, max_depth
        total_nodes += 1
        max_depth = max(max_depth, depth)

        if isinstance(node, (ast.For, ast.While)):
            loops += 1
        if isinstance(node, ast.If):
            branches += 1
        if isinstance(node, ast.BoolOp):
            bool_ops += 1
        if isinstance(node, ast.Call):
            calls += 1
        if isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)):
            comps += 1

        for child in ast.iter_child_nodes(node):
            visit(child, depth + 1)

    visit(tree)

    raw = (
        8 * loops +
        6 * branches +
        3 * bool_ops +
        1.5 * calls +
        6 * comps +
        2.0 * max_depth +
        0.12 * total_nodes
    )

    # Smoothly squash to 0–100
    score = 100 * (1 - math.exp(-raw / 30))
    return max(0.0, min(100.0, score))


def pick_variants_by_target(variants: list[str], target: float, k: int = 10, tol: float = 10.0) -> list[str]:
    """
    Pick k variants closest to target difficulty.
    Prefer variants within tol; if not enough, take closest overall.
    """
    scored = []
    for v in variants:
        s = difficulty_score(v)
        scored.append((abs(s - target), s, v))

    scored.sort(key=lambda x: x[0])  # closest first

    within = [v for diff, s, v in scored if diff <= tol]
    if len(within) >= k:
        return within[:k]

    return [v for diff, s, v in scored[:k]]


# -------------------------
# Model calling
# -------------------------
def complete(prompt: str, system: str, max_retries: int = 5) -> str:
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="zai-org/GLM-5",
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": prompt},
                ],
            )
            return response.model_dump()["choices"][0]["message"]["content"]
        except Exception as e:
            if "rate" in str(e).lower() or "429" in str(e):
                wait_time = (2 ** attempt) + 1
                print(f"Warning: Rate limit hit. Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                raise e
    raise Exception("Max retries exceeded")


# -------------------------
# Variant generation + filtering
# -------------------------
def generate_variants(problem: str) -> dict:
    system_prompt = """You are an expert at creating programming problem variants. 
Given a Python programming puzzle in the format `assert f(g())`, generate variants that:
1. Stay within the same problem class (same type of algorithm/logic)
2. Have easier difficulty than the original
3. Maintain the same format with assert statements
4. Are complete, self-contained problems

Return ONLY the variants as a JSON list of strings, with no additional text or markdown formatting."""

    result = {"easy": [], "medium": [], "hard": [problem]}

    # Quantify original difficulty and set numeric targets
    D = difficulty_score(problem)
    target_medium = 0.70 * D
    target_easy = 0.30 * D

    medium_prompt = f"""Generate 10 variants of this Python programming puzzle at approximately 70% of the original difficulty (slightly easier but still challenging):

{problem}

Return as a JSON list of strings containing only the assert statements."""

    medium_response = complete(medium_prompt, system_prompt)
    try:
        medium_list = json.loads(medium_response)
        if not isinstance(medium_list, list):
            medium_list = [medium_response]
    except json.JSONDecodeError:
        medium_list = [medium_response]

    # Filter medium variants to be closest to target_medium
    result["medium"] = pick_variants_by_target(medium_list, target_medium, k=10, tol=10.0)

    easy_prompt = f"""Generate 10 variants of this Python programming puzzle at approximately 30% of the original difficulty (much simpler, suitable for beginners):

{problem}

Return as a JSON list of strings containing only the assert statements."""

    # Collect more easy candidates, then filter down to the best 10
    easy_all = []
    for _ in range(3):
        easy_response = complete(easy_prompt, system_prompt)
        try:
            easy_list = json.loads(easy_response)
            if isinstance(easy_list, list):
                easy_all.extend(easy_list)
            else:
                easy_all.append(easy_response)
        except json.JSONDecodeError:
            easy_all.append(easy_response)

    result["easy"] = pick_variants_by_target(easy_all, target_easy, k=10, tol=12.0)

    # Optional: print a quick check so you can see it's working
    # print(f"Original: {D:.1f} | Easy target: {target_easy:.1f} | Medium target: {target_medium:.1f}")

    return result


def sanitize_name(name: str) -> str:
    return re.sub(r'[<>:"/\\|?*]', "-", name)


def process_puzzles(input_path: str, output_dir: str = "outputs"):
    os.makedirs(output_dir, exist_ok=True)

    with open(input_path, "r") as f:
        puzzles = json.load(f)

    for puzzle in tqdm(puzzles, desc="Processing puzzles"):
        name = sanitize_name(puzzle["name"])
        problem = f"{puzzle['sat']}"

        variants = generate_variants(problem)

        output_path = os.path.join(output_dir, f"problem_{name}_variants.json")
        with open(output_path, "w") as f:
            json.dump(variants, f, indent=2)


if __name__ == "__main__":
    print("Script started")
    process_puzzles("puzzles.json")
    print("Script finished")