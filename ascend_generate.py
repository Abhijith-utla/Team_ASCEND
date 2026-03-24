"""
Ascend — Variant Generation Pipeline
=====================================
Generates root coding problems + recursive variant trees for RL training.

Setup:
    pip install groq

Usage:
    export GROQ_API_KEY="your-key-here"
    python ascend_generate.py

Get a free Groq API key at: https://console.groq.com

Output:
    ascend_variants.json
"""

import os
import json
import random
import time
from datetime import datetime

from groq import Groq

# ── Config ────────────────────────────────────────────────────────────────────

CONFIG = {
    "num_roots": 10,          # Number of root (hardest) problems to generate
    "variants_per_node": 2,   # How many children each node spawns
    "tree_depth": 2,          # How many levels deep the variant tree goes
    "model": "llama-3.3-70b-versatile",  # Free on Groq, very capable
    "max_tokens": 1500,
    "retry_attempts": 3,      # Retries on API/parse failures
    "retry_delay": 2,         # Seconds between retries
}

# ── Topics & Difficulties ─────────────────────────────────────────────────────

TOPICS = [
    "Arrays & Hashing",
    "Two Pointers",
    "Sliding Window",
    "Binary Search",
    "Linked Lists",
    "Trees",
    "Graphs",
    "Dynamic Programming",
    "Greedy",
    "Stack & Queue",
]

DIFFICULTY_LEVELS = ["Easy", "Medium", "Hard"]

PERSONAS = [
    "competitive programmer designing warm-up problems",
    "CS professor isolating a single concept for beginners",
    "coding bootcamp instructor building a learning ladder",
    "technical interviewer creating entry-level screening questions",
    "curriculum designer focused on incremental skill building",
]

# ── Prompts ───────────────────────────────────────────────────────────────────

def root_prompt(topic: str, difficulty: str) -> str:
    return f"""You are designing coding problems for an AI training dataset called Ascend.

Generate ONE original coding problem with these requirements:
- Topic: {topic}
- Difficulty: {difficulty} (LeetCode scale)
- Must be clearly solvable, unambiguous, with a single correct approach
- Include 1-2 concrete example inputs/outputs
- Do NOT copy famous LeetCode problems verbatim — create original variants

Respond ONLY with valid JSON, no markdown, no explanation:
{{
  "title": "Problem title",
  "difficulty": "{difficulty}",
  "topic": "{topic}",
  "description": "Full problem description with examples",
  "constraints": ["constraint 1", "constraint 2"],
  "core_technique": "The main algorithm/technique required",
  "insight": "The key insight needed to solve this",
  "expected_complexity": {{ "time": "O(?)", "space": "O(?)" }}
}}"""


def variant_prompt(parent: dict, target_difficulty: str, batch_size: int, persona: str) -> str:
    return f"""You are a {persona} helping build a training curriculum for AI models.

Given this coding problem:
TITLE: {parent["title"]}
DESCRIPTION: {parent["description"]}
CORE TECHNIQUE: {parent["core_technique"]}
DIFFICULTY: {parent["difficulty"]}

Generate {batch_size} DISTINCT coding problem variants that are {target_difficulty} than the parent.

Rules:
- Each variant must be a SIMPLER or EQUIVALENT version (never harder)
- Simpler = relax constraints, reduce dimensions, remove edge cases, decompose the technique
- Equivalent = same difficulty but different domain or framing
- Each variant must still be a valid, solvable coding problem
- Keep variants in the same general topic area

Respond ONLY with a valid JSON array, no markdown, no explanation:
[
  {{
    "title": "Variant title",
    "difficulty": "Easy|Easy-Medium|Medium",
    "difficulty_delta": "much_easier|easier|equivalent",
    "description": "Full problem description with examples",
    "constraints": ["constraint 1"],
    "core_technique": "Main technique required",
    "insight": "Key insight",
    "expected_complexity": {{ "time": "O(?)", "space": "O(?)" }},
    "relationship_to_parent": "How this differs (e.g. removed DP layer, now just greedy)",
    "simplification_type": "constraint_relaxation|domain_swap|technique_decomposition|edge_case_removal|dimension_reduction"
  }}
]"""


# ── API Helper ────────────────────────────────────────────────────────────────

def call_groq(client: Groq, prompt: str) -> dict | list:
    """Call Groq and parse JSON response. Retries on failure."""
    for attempt in range(CONFIG["retry_attempts"]):
        try:
            response = client.chat.completions.create(
                model=CONFIG["model"],
                max_tokens=CONFIG["max_tokens"],
                messages=[{"role": "user", "content": prompt}],
            )
            text = response.choices[0].message.content.strip()
            # Strip markdown code fences if present
            text = text.replace("```json", "").replace("```", "").strip()
            return json.loads(text)
        except json.JSONDecodeError as e:
            print(f"    ⚠ JSON parse error (attempt {attempt + 1}): {e}")
        except Exception as e:
            print(f"    ⚠ API error (attempt {attempt + 1}): {e}")
        if attempt < CONFIG["retry_attempts"] - 1:
            time.sleep(CONFIG["retry_delay"])
    raise RuntimeError("All retry attempts failed")


# ── Pipeline Stages ───────────────────────────────────────────────────────────

def generate_roots(client: Groq) -> list[dict]:
    """Generate root (hardest) problems — one per topic."""
    print("\n🌱 Stage 1: Generating root problems")
    print("─" * 50)

    topics = random.sample(TOPICS, CONFIG["num_roots"])
    roots = []

    for i, topic in enumerate(topics):
        difficulty = random.choice(DIFFICULTY_LEVELS)
        print(f"  [{i+1}/{CONFIG['num_roots']}] {topic} ({difficulty})...", end=" ", flush=True)

        try:
            root = call_groq(client, root_prompt(topic, difficulty))
            root["id"] = f"root_{i}"
            root["depth"] = 0
            root["parent_id"] = None
            root["children"] = []
            roots.append(root)
            print(f'✓ "{root["title"]}"')
        except Exception as e:
            print(f"✗ Failed: {e}")

    return roots


def generate_variant_tree(client: Groq, roots: list[dict]) -> list[dict]:
    """
    For each root, recursively generate a tree of simpler variants via BFS.
    Returns all nodes (roots + variants) as a flat list.
    """
    print("\n🌿 Stage 2: Generating variant trees")
    print("─" * 50)

    all_nodes = list(roots)

    for root in roots:
        print(f'\n  Tree for: "{root["title"]}"')
        queue = [root]

        while queue:
            parent = queue.pop(0)
            if parent["depth"] >= CONFIG["tree_depth"]:
                continue

            persona = random.choice(PERSONAS)
            target_diff = "much easier" if parent["depth"] >= 1 else "easier"
            next_depth = parent["depth"] + 1

            print(f"    Depth {parent['depth']}→{next_depth}: generating {CONFIG['variants_per_node']} variants...", end=" ", flush=True)

            try:
                variants = call_groq(
                    client,
                    variant_prompt(parent, target_diff, CONFIG["variants_per_node"], persona)
                )

                if not isinstance(variants, list):
                    print("✗ Response was not a list")
                    continue

                for idx, v in enumerate(variants[:CONFIG["variants_per_node"]]):
                    v["id"] = f"{parent['id']}_v{idx}"
                    v["depth"] = next_depth
                    v["parent_id"] = parent["id"]
                    v["children"] = []
                    parent["children"].append(v["id"])
                    all_nodes.append(v)
                    queue.append(v)

                print(f"✓ {len(variants)} variants")

            except Exception as e:
                print(f"✗ Failed: {e}")

    return all_nodes


def build_dataset(all_nodes: list[dict]) -> dict:
    """Assemble final JSON dataset with metadata and stats."""
    difficulty_dist = {}
    simplification_types = {}
    topics_covered = set()

    for node in all_nodes:
        d = node.get("difficulty", "Unknown")
        difficulty_dist[d] = difficulty_dist.get(d, 0) + 1

        s = node.get("simplification_type")
        if s:
            simplification_types[s] = simplification_types.get(s, 0) + 1

        t = node.get("topic")
        if t:
            topics_covered.add(t)

    return {
        "meta": {
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "pipeline": "Ascend Variant Generator v1.0",
            "config": CONFIG,
            "stats": {
                "total_problems": len(all_nodes),
                "root_problems": sum(1 for n in all_nodes if n["depth"] == 0),
                "total_variants": sum(1 for n in all_nodes if n["depth"] > 0),
                "topics_covered": sorted(topics_covered),
                "difficulty_distribution": difficulty_dist,
                "simplification_types": simplification_types,
                "depth_distribution": {
                    str(d): sum(1 for n in all_nodes if n["depth"] == d)
                    for d in sorted(set(n["depth"] for n in all_nodes))
                },
            },
        },
        "problems": all_nodes,
    }


def print_summary(dataset: dict):
    stats = dataset["meta"]["stats"]
    print("\n📊 Dataset Summary")
    print("─" * 50)
    print(f"  Total problems    : {stats['total_problems']}")
    print(f"  Root problems     : {stats['root_problems']}")
    print(f"  Variants          : {stats['total_variants']}")
    print(f"  Topics covered    : {', '.join(stats['topics_covered'])}")
    print(f"  Difficulty dist   : {stats['difficulty_distribution']}")
    print(f"  Depth dist        : {stats['depth_distribution']}")
    print(f"  Simplif. types    : {stats['simplification_types']}")


# ── Entry Point ───────────────────────────────────────────────────────────────

def main():
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "GROQ_API_KEY not set.\n"
            "Get a free key at https://console.groq.com\n"
            "Then run: export GROQ_API_KEY='your-key-here'"
        )

    client = Groq(api_key=api_key)

    print("⚡ ASCEND — Variant Generation Pipeline")
    print("=" * 50)
    print(f"  Roots         : {CONFIG['num_roots']}")
    print(f"  Variants/node : {CONFIG['variants_per_node']}")
    print(f"  Tree depth    : {CONFIG['tree_depth']}")
    print(f"  Model         : {CONFIG['model']}")

    # Stage 1: roots
    roots = generate_roots(client)

    # Stage 2: variant trees
    all_nodes = generate_variant_tree(client, roots)

    # Stage 3: assemble dataset
    print("\n📦 Stage 3: Building dataset...")
    dataset = build_dataset(all_nodes)

    # Save
    output_path = "ascend_variants.json"
    with open(output_path, "w") as f:
        json.dump(dataset, f, indent=2)

    print_summary(dataset)
    print(f"\n✅ Saved to {output_path}")


if __name__ == "__main__":
    main()