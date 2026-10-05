"""Build a module-level train/val/test split for P3 puzzles.

Whole P3 modules (the `module` field) are assigned to one split, so the test set
measures generalization to unseen puzzle families rather than unseen puzzles
from known families.

Usage:
    python scripts/make_split.py --seed 0
"""

import argparse
import hashlib
import json
import random
from collections import defaultdict
from pathlib import Path

PUZZLES = Path("PythonProgrammingPuzzles/puzzles/puzzles.json")
OUT_DIR = Path("data/splits")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_split(puzzles: list[dict], seed: int, test_frac: float, val_frac: float) -> dict:
    by_module: dict[str, list[int]] = defaultdict(list)
    for idx, p in enumerate(puzzles):
        by_module[p["module"]].append(idx)

    modules = sorted(by_module)
    random.Random(seed).shuffle(modules)

    total = len(puzzles)
    split_modules: dict[str, list[str]] = {"test": [], "val": [], "train": []}
    counts = {"test": 0, "val": 0, "train": 0}

    # Greedily fill test, then val, until each reaches its target fraction.
    # Remaining modules go to train. Whole modules only, so sizes are approximate.
    targets = {"test": test_frac * total, "val": val_frac * total}
    for name in ("test", "val"):
        while modules and counts[name] < targets[name]:
            m = modules.pop()
            split_modules[name].append(m)
            counts[name] += len(by_module[m])
    split_modules["train"] = modules
    counts["train"] = sum(len(by_module[m]) for m in modules)

    indices = {k: sorted(i for m in v for i in by_module[m]) for k, v in split_modules.items()}
    return {"seed": seed, "modules": split_modules, "counts": counts, "indices": indices}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--test-frac", type=float, default=0.30)
    ap.add_argument("--val-frac", type=float, default=0.10)
    args = ap.parse_args()

    puzzles = json.loads(PUZZLES.read_text(encoding="utf-8"))
    split = build_split(puzzles, args.seed, args.test_frac, args.val_frac)
    split["source"] = str(PUZZLES)
    split["source_sha256"] = sha256(PUZZLES)
    split["total"] = len(puzzles)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f"p3_module_split_seed{args.seed}.json"
    out.write_text(json.dumps(split, indent=2), encoding="utf-8")

    c = split["counts"]
    print(f"wrote {out}")
    print(f"train={c['train']} val={c['val']} test={c['test']} total={split['total']}")
    print("test modules:", split["modules"]["test"])
    print("val modules:", split["modules"]["val"])


if __name__ == "__main__":
    main()
