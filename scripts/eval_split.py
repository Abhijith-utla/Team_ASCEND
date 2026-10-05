"""Greedy pass@1 of a base or trained model on a P3 split.

Uses V1's verifier (ladder_optimizer_v4.LadderOptimizer) so numbers are
comparable with the V1 logs. Only puzzles in the chosen split are scored.

Usage (Colab, from the repo root):
    python scripts/eval_split.py --split test --seed 0
    python scripts/eval_split.py --split val  --seed 0 --model deepseek-ai/deepseek-coder-1.3b-instruct
"""

import argparse
import json
from pathlib import Path

from datasets import Dataset

import ladder_optimizer_v4 as lo

PUZZLES = Path("PythonProgrammingPuzzles/puzzles/puzzles.json")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", choices=["train", "val", "test"], required=True)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--model", default="deepseek-ai/deepseek-coder-1.3b-instruct")
    ap.add_argument("--out", default=None, help="Optional JSON path for the result")
    args = ap.parse_args()

    puzzles = json.loads(PUZZLES.read_text(encoding="utf-8"))
    split = json.loads(Path(f"data/splits/p3_module_split_seed{args.seed}.json").read_text())
    idxs = split["indices"][args.split]

    items = [
        {
            "prompt": puzzles[i]["sat"],
            "sat_code": puzzles[i]["sat"],
            "problem_id": f"p3_{i:05d}_{puzzles[i]['name']}",
            "difficulty": "hard",
            "variant_num": 0,
        }
        for i in idxs
    ]
    print(f"Evaluating {len(items)} '{args.split}' puzzles with {args.model}")

    model, tokenizer, has_chat = lo.load_default_model(args.model)
    opt = lo.LadderOptimizer(
        Dataset.from_list([{"prompt": x["prompt"]} for x in items]),
        model,
        tokenizer,
        debug=False,
        has_native_chat_template=has_chat,
    )
    # Greedy, one sample per puzzle: pass@1.
    result = opt.evaluate_performance(Dataset.from_list(items), num_samples=1, do_sample=False)
    score = result.get("hard", 0.0)

    print(f"\n{args.split} greedy pass@1 = {score:.4f}  (n={len(items)})")
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(
            json.dumps(
                {
                    "split": args.split,
                    "seed": args.seed,
                    "model": args.model,
                    "n": len(items),
                    "pass_at_1_greedy": score,
                },
                indent=2,
            )
        )


if __name__ == "__main__":
    main()
