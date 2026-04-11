#!/usr/bin/env python3

import json
import os
from datetime import datetime, timezone
from pathlib import Path

from datasets import Dataset

import ladder_optimizer_v4 as lo
import variant_generator_v2 as vg


PUZZLES_PATH = "PythonProgrammingPuzzles/puzzles/puzzles.json"
MODEL_ID = "deepseek-ai/deepseek-coder-1.3b-instruct"
RUNS_ROOT = Path("training_runs")

# Set to None to use all puzzles.
PROBLEM_LIMIT = 100

TRAINING_HYPERPARAMS = {
    "max_steps": 20,
    "target_accuracy": 0.8,
    "learning_rate": 5e-6,
    "group_size": 4,
    "exec_timeout_seconds": 1.0,
}


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def sanitize_name(text: str) -> str:
    out = []
    for ch in text:
        if ch.isalnum() or ch in ("-", "_"):
            out.append(ch)
        else:
            out.append("_")
    cleaned = "".join(out).strip("_")
    return cleaned or "unnamed"


def load_puzzles(path: str = PUZZLES_PATH) -> list[dict]:
    if not os.path.exists(path):
        raise FileNotFoundError(f"puzzles.json not found at: {path}")

    with open(path, "r", encoding="utf-8") as f:
        puzzles = json.load(f)

    if not puzzles:
        raise ValueError("No puzzles found")

    return puzzles


def build_problem_id(index: int, puzzle: dict) -> str:
    name = puzzle.get("name", f"problem_{index}")
    return f"{index:05d}_{sanitize_name(name)}"


def list_numeric_run_ids(runs_root: Path) -> list[int]:
    if not runs_root.exists():
        return []

    out = []
    for child in runs_root.iterdir():
        if child.is_dir() and child.name.isdigit():
            out.append(int(child.name))
    return sorted(out)


def next_run_id(runs_root: Path) -> str:
    existing = list_numeric_run_ids(runs_root)
    next_id = (existing[-1] + 1) if existing else 1
    return f"{next_id:05d}"


def load_run_json(run_dir: Path) -> dict:
    run_json_path = run_dir / "run.json"
    if not run_json_path.exists():
        raise FileNotFoundError(f"Missing run.json in {run_dir}")
    with open(run_json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_run_json(run_dir: Path, data: dict):
    run_json_path = run_dir / "run.json"
    with open(run_json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True)


def find_latest_incomplete_run(runs_root: Path) -> Path | None:
    for run_id in reversed(list_numeric_run_ids(runs_root)):
        run_dir = runs_root / f"{run_id:05d}"
        run_json_path = run_dir / "run.json"
        if not run_json_path.exists():
            continue
        try:
            data = load_run_json(run_dir)
        except Exception:
            continue
        if data.get("status") != "completed":
            return run_dir
    return None


def prompt_resume_run(run_dir: Path) -> bool:
    run_data = load_run_json(run_dir)
    completed = len(run_data.get("completed_problem_indices", []))
    total = run_data.get("problem_limit_effective", "?")
    print(
        f"Found incomplete run {run_dir.name} with {completed}/{total} completed problems."
    )
    answer = input("Resume from the most recent checkpoint? [y/N]: ").strip().lower()
    return answer in {"y", "yes"}


def initialize_new_run(
    runs_root: Path,
    model_id: str,
    problem_limit_effective: int,
    hyperparams: dict,
) -> tuple[str, Path, dict]:
    run_id = next_run_id(runs_root)
    run_dir = runs_root / run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    (run_dir / "artifacts").mkdir(parents=True, exist_ok=True)

    run_data = {
        "run_id": run_id,
        "status": "running",
        "created_at": utc_now_iso(),
        "updated_at": utc_now_iso(),
        "model_id": model_id,
        "problem_limit_effective": problem_limit_effective,
        "completed_problem_indices": [],
        "completed_problem_ids": [],
        "latest_checkpoint": None,
        "problem_checkpoints": {},
        "pretrain_evaluated": False,
        "hyperparameters": hyperparams,
    }
    save_run_json(run_dir, run_data)
    return run_id, run_dir, run_data


def resolve_run(
    runs_root: Path,
    model_id: str,
    problem_limit_effective: int,
    hyperparams: dict,
) -> tuple[str, Path, dict, bool]:
    runs_root.mkdir(parents=True, exist_ok=True)
    latest_incomplete = find_latest_incomplete_run(runs_root)

    if latest_incomplete is not None and prompt_resume_run(latest_incomplete):
        run_data = load_run_json(latest_incomplete)
        run_data["updated_at"] = utc_now_iso()
        save_run_json(latest_incomplete, run_data)
        return run_data["run_id"], latest_incomplete, run_data, True

    run_id, run_dir, run_data = initialize_new_run(
        runs_root=runs_root,
        model_id=model_id,
        problem_limit_effective=problem_limit_effective,
        hyperparams=hyperparams,
    )
    return run_id, run_dir, run_data, False


def main():
    puzzles = load_puzzles()

    print(f"Total puzzles: {len(puzzles)}")
    print("Keys in each puzzle:", puzzles[0].keys())
    print("\n--- Example puzzle ---")
    print(puzzles[0])

    base_puzzles = puzzles[:PROBLEM_LIMIT] if PROBLEM_LIMIT is not None else puzzles
    problem_limit_effective = len(base_puzzles)

    run_id, run_dir, run_data, resumed = resolve_run(
        runs_root=RUNS_ROOT,
        model_id=MODEL_ID,
        problem_limit_effective=problem_limit_effective,
        hyperparams=TRAINING_HYPERPARAMS,
    )

    print(f"Run ID: {run_id}")
    if resumed:
        print("Resuming previous run.")
    else:
        print("Starting new run.")

    model, tokenizer, has_native_chat_template = lo.load_default_model(MODEL_ID)
    print("Model loaded!")
    print(f"Model ID: {MODEL_ID}")
    print(f"Using native chat template: {has_native_chat_template}")

    optimizer = lo.LadderOptimizer(
        model=model,
        tokenizer=tokenizer,
        run_dir=run_dir,
        debug=False,
        has_native_chat_template=has_native_chat_template,
        exec_timeout_seconds=TRAINING_HYPERPARAMS["exec_timeout_seconds"],
    )

    latest_checkpoint = run_data.get("latest_checkpoint")
    if latest_checkpoint:
        latest_checkpoint_path = Path(latest_checkpoint)
        if latest_checkpoint_path.exists():
            print(f"Loading checkpoint from: {latest_checkpoint_path}")
            optimizer.load_adapter_checkpoint(latest_checkpoint_path)
        else:
            print(f"[WARN] latest checkpoint path does not exist: {latest_checkpoint_path}")

    base_dataset = [
        {
            "prompt": puzzle["sat"],
            "problem_id": build_problem_id(i, puzzle),
            "variant_num": 0,
            "source_name": puzzle.get("name", f"problem_{i}"),
            "notes": puzzle.get("notes", ""),
        }
        for i, puzzle in enumerate(base_puzzles)
    ]
    print(f"Prepared {len(base_dataset)} problems for this run")

    completed_indices = set(run_data.get("completed_problem_indices", []))
    remaining = [i for i in range(len(base_dataset)) if i not in completed_indices]
    print(f"Remaining problems to train: {len(remaining)}")

    if not run_data.get("pretrain_evaluated", False):
        print("\n=== Evaluate Pre-train accuracy ===")
        pre_eval_dataset = Dataset.from_list(base_dataset)
        optimizer.evaluate_performance(pre_eval_dataset)

        run_data = load_run_json(run_dir)
        run_data["pretrain_evaluated"] = True
        run_data["updated_at"] = utc_now_iso()
        save_run_json(run_dir, run_data)
    else:
        print("\n=== Skipping Pre-train accuracy (already completed for this run) ===")

    print("\n=== Beginning Train Loop ===")
    for i, problem in enumerate(base_dataset):
        if i in completed_indices:
            print(f"Skipping already completed problem {i + 1}/{len(base_dataset)}: {problem['problem_id']}")
            continue

        problem_id = problem["problem_id"]
        problem_dir = run_dir / problem_id
        artifacts_dir = problem_dir / "artifacts"
        artifacts_dir.mkdir(parents=True, exist_ok=True)

        print(f"    Starting problem {i + 1} of {len(base_dataset)}: {problem_id}")

        print("    Generating variant tree... ", end="")
        tree = vg.generate_variant_tree(
            model=model,
            tokenizer=tokenizer,
            has_native_chat_template=has_native_chat_template,
            sat_code=problem["prompt"],
            notes=problem.get("notes", "No description available"),
            problem_id=problem_id,
            run_dir=run_dir,
            max_new_tokens=800,
            max_retries=3,
        )
        print("Done!")

        print("    --- Variant Tree Summary (filtering disabled) ---")
        print(f"        hard:   {len(tree['hard'])}")
        print(f"        medium: {len(tree['medium'])}")
        print(f"        easy:   {len(tree['easy'])}")
        print()

        print("    --- Begin Training ---")
        optimizer.train_on_tree(
            problem_id=problem_id,
            tree=tree,
            max_steps=TRAINING_HYPERPARAMS["max_steps"],
            target_accuracy=TRAINING_HYPERPARAMS["target_accuracy"],
            learning_rate=TRAINING_HYPERPARAMS["learning_rate"],
            group_size=TRAINING_HYPERPARAMS["group_size"],
            problem_artifacts_dir=artifacts_dir,
        )

        checkpoint_path = optimizer.save_problem_checkpoint(problem_id=problem_id)
        print(f"    Saved checkpoint: {checkpoint_path}")

        run_data = load_run_json(run_dir)
        run_data["completed_problem_indices"] = sorted(
            set(run_data.get("completed_problem_indices", [])) | {i}
        )
        run_data["completed_problem_ids"] = sorted(
            set(run_data.get("completed_problem_ids", [])) | {problem_id}
        )
        run_data.setdefault("problem_checkpoints", {})
        run_data["problem_checkpoints"][problem_id] = str(checkpoint_path)
        run_data["latest_checkpoint"] = str(checkpoint_path)
        run_data["updated_at"] = utc_now_iso()
        save_run_json(run_dir, run_data)

    print("\n=== Evaluate Post-train accuracy ===")
    post_eval_dataset = Dataset.from_list(base_dataset)
    optimizer.evaluate_performance(post_eval_dataset)

    final_path = optimizer.save_final_checkpoint()
    print(f"Final model saved to: {final_path}")

    run_data = load_run_json(run_dir)
    run_data["status"] = "completed"
    run_data["latest_checkpoint"] = str(final_path)
    run_data["final_checkpoint"] = str(final_path)
    run_data["updated_at"] = utc_now_iso()
    save_run_json(run_dir, run_data)


if __name__ == "__main__":
    main()
