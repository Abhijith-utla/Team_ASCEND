import re
from datasets import Dataset

def estimate_difficulty(model, tokenizer, sat_code: str, n_attempts: int = 10) -> float:
    """
    Estimate difficulty as solve rate: fraction of n_attempts where
    the model generates a valid solution (i.e. sat(solution) == True).
    Returns a float in [0, 1] where lower = harder.
    """
    prompt = f"""Solve this Python Programming Puzzle. The function sat() returns True if your answer is correct.
Write ONLY a single Python expression that, when passed to sat(), returns True.

{sat_code}

Answer (a single Python expression):"""

    messages = [{"role": "user", "content": prompt}]
    text = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    inputs = tokenizer([text], return_tensors="pt").to(model.device)

    successes = 0
    for _ in range(n_attempts):
        with torch.no_grad():
            output_ids = model.generate(
                **inputs,
                max_new_tokens=200,
                temperature=0.8,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id,
            )
        generated = output_ids[0][inputs["input_ids"].shape[1]:]
        raw = tokenizer.decode(generated, skip_special_tokens=True).strip()

        # Extract just the first line / expression
        candidate = raw.splitlines()[0].strip()

        try:
            # Build a safe local namespace, execute sat, test candidate
            local_ns = {}
            exec(sat_code, local_ns)
            sat_fn = local_ns.get("sat")
            if sat_fn is None:
                continue
            result = eval(candidate, local_ns)
            if sat_fn(result):
                successes += 1
        except Exception:
            pass

    return successes / n_attempts


def filter_tree_by_difficulty(
    tree: dict,
    model,
    tokenizer,
    low: float = 0.30,
    high: float = 0.70,
    n_attempts: int = 10,
) -> dict:
    """
    Takes a variant tree (keys: 'hard', 'medium', 'easy'), evaluates each
    problem's solve rate, and keeps only problems with solve rate in [low, high].
    Problems outside that range are discarded.
    """
    filtered = {}

    for tier, problems in tree.items():
        kept = []
        for prob in problems:
            sat_code = prob["prompt"]
            solve_rate = estimate_difficulty(model, tokenizer, sat_code, n_attempts)
            in_range = low <= solve_rate <= high
            print(
                f"  [{tier}] solve_rate={solve_rate:.2f} "
                f"{'KEEP' if in_range else 'DROP'} — "
                f"{sat_code[:60].strip()!r}..."
            )
            if in_range:
                kept.append({**prob, "solve_rate": solve_rate})

        print(f"  {tier}: kept {len(kept)}/{len(problems)} problems")
        filtered[tier] = kept

    return filtered


# ── Drop-in replacement for the train loop ────────────────────────────────────

print("\n=== Beginning Train Loop (with difficulty filtering) ===")

for i, problem in enumerate(base_dataset):
    sat_code = problem["prompt"]
    print(f"\n--- Problem {i+1}/{len(base_dataset)} ---")

    print("  Generating variant tree...", end=" ")
    tree = generate_variant_tree(model, sat_code, "No description available")
    print("done.")

    print("  Filtering variants to 30–70% solve rate...")
    tree = filter_tree_by_difficulty(tree, model, tokenizer, low=0.30, high=0.70)

    # Skip training if filtering left nothing useful
    total_variants = sum(len(v) for k, v in tree.items() if k != "hard")
    if total_variants == 0:
        print("  No variants survived filtering — skipping this problem.")
        continue

    print("  Creating LadderOptimizer...")
    opt = lo.LadderOptimizer(tree, model, tokenizer)

    print("  Training...")
    opt.train(max_steps=20, target_accuracy=0.8, learning_rate=5e-6, group_size=4)

    model = opt.model