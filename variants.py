import os
import json
import time
import re
from openai import OpenAI
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()

client = OpenAI(
    base_url="https://api.featherless.ai/v1",
    api_key=os.environ.get("FEATHERLESS_API_KEY"),
)


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


def generate_variants(problem: str) -> dict:
    system_prompt = """You are an expert at creating programming problem variants. 
Given a Python programming puzzle in the format `assert f(g())`, generate variants that:
1. Stay within the same problem class (same type of algorithm/logic)
2. Have easier difficulty than the original
3. Maintain the same format with assert statements
4. Are complete, self-contained problems

Return ONLY the variants as a JSON list of strings, with no additional text or markdown formatting."""

    result = {"easy": [], "medium": [], "hard": [problem]}

    medium_prompt = f"""Generate 10 variants of this Python programming puzzle at approximately 70% of the original difficulty (slightly easier but still challenging):

{problem}

Return as a JSON list of strings containing only the assert statements."""

    medium_response = complete(medium_prompt, system_prompt)
    try:
        result["medium"] = json.loads(medium_response)
    except json.JSONDecodeError:
        result["medium"] = [medium_response]

    easy_prompt = f"""Generate 10 variants of this Python programming puzzle at approximately 30% of the original difficulty (much simpler, suitable for beginners):

{problem}

Return as a JSON list of strings containing only the assert statements."""

    for _ in range(3):
        easy_response = complete(easy_prompt, system_prompt)
        try:
            result["easy"].extend(json.loads(easy_response))
        except json.JSONDecodeError:
            result["easy"].append(easy_response)

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
    process_puzzles("puzzles.json")
