from ladder_optimizer import LadderOptimizer, load_default_model

model, tokenizer = load_default_model()

dataset = {
    "easy": [
        {
            "id": "easy_001",
            "prompt": (
                "def sat(l):\n"
                "    return l == [1, 2, 3]\n"
            ),
        },
    ],
    "medium": [
        {
            "id": "medium_001",
            "prompt": (
                "def sat(l):\n"
                "    return l == list(range(0, 10, 2))\n"
            ),
        },
    ],
    "hard": [
        {
            "id": "hard_001",
            "prompt": (
                "def sat(l):\n"
                "    return all(i != j for i, j in zip(l, range(999))) and sorted(l) == list(range(999))\n"
            ),
        },
    ],
}

trainer = LadderOptimizer(dataset, model, tokenizer)

print("\n=== Evaluate Pre-train accuracy ===")

trainer.evaluate_performance()
print("\n=== Pre-train Sample Generation ===")
test_prompt = dataset["hard"][0]["prompt"]
print(trainer.generate(test_prompt))

print("\n=== Begin Training ===")

trainer.train(
    max_steps=20,
    target_accuracy=0.8,
    learning_rate=5e-6,
    group_size=4,
)

print("\n=== Evaluate Post-train accuracy ===")

trainer.evaluate_performance()
print("\n=== Post-train Sample Generation ===")
test_prompt = dataset["hard"][0]["prompt"]
print(trainer.generate(test_prompt))
