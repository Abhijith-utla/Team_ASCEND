import os
import re
import torch
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import LoraConfig
from trl import GRPOConfig, GRPOTrainer

MODEL_ID = "Qwen/Qwen2.5-Coder-3B-Instruct"

# Replace with generated variants
train_dataset = Dataset.from_list(
    [
        {
            "prompt": (
                "Write Python code that defines a function sol() that returns a derangement of range(999).\n"
                "Your response must contain ONLY the Python code for the sol() function and any necessary imports.\n"
                "Do NOT include any explanations, comments outside the code, or markdown formatting.\n"
                "Example format:\n"
                "import itertools\n"
                "def sol():\n"
                "    return list(itertools.permutations(range(999)))[1:]\n"
            )
        },
        {
            "prompt": (
                "Write Python code that defines a function sol() that returns the list [1,2,3].\n"
                "Your response must contain ONLY the Python code for the sol() function and any necessary imports.\n"
                "Do NOT include any explanations, comments outside the code, or markdown formatting.\n"
                "Example format:\n"
                "def sol():\n"
                "    return [1,2,3]\n"
            )
        },
    ]
)


def reward_func(prompts, completions, **kwargs):
    # Updated reward: check if completion contains valid Python code defining sol()
    rewards = []
    for p, c in zip(prompts, completions):
        # Extract sat_code from prompt (which still has code block format for now)
        pattern = re.compile(
            r"```[ \t]*([A-Za-z0-9_+-]+)?[ \t]*\n"  # optional language tag (group 1)
            r"([\s\S]*?)"  # code (group 2)
            r"\n```"  # closing fence
        )

        sat = re.search(pattern, p)
        if not sat:
            raise ValueError(f"Failed to extract sat from prompt {p}")

        sat_code = sat.group(2).strip()

        # For completion, we expect raw Python code (no code blocks)
        sol_code = c.strip()

        test_string = f"{sat_code}\n\n{sol_code}\n\nassert sat(sol())"
        try:
            glb = {}
            exec(test_string, glb, glb)
            rewards.append(1.0)
        except:
            rewards.append(0.0)
    return rewards


tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID, torch_dtype=torch.float16, device_map=None, low_cpu_mem_usage=True
).to("cuda")

# ChatGPT suggested options, potentially subject to further research and tuning later on
training_args = GRPOConfig(
    output_dir="grpo_out",
    per_device_train_batch_size=1,  # start small
    gradient_accumulation_steps=4,  # accumulate to simulate larger batch
    learning_rate=5e-6,
    max_steps=20,  # small demo run; increase for real training
    logging_steps=1,
    num_generations=4,  # GRPO group size G
    max_completion_length=256,
    temperature=0.8,
    top_p=0.95,
    # For consumer GPUs, fp16 usually helps.
    fp16=True,
    # You can pass kwargs to from_pretrained here (e.g. quantization).
    model_init_kwargs={
        "torch_dtype": torch.float16,
        "device_map": "auto",
        # If you want 4-bit loading, uncomment these and ensure bitsandbytes is installed:
        # "load_in_4bit": True,
    },
)

peft_config = LoraConfig(
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
    target_modules=[
        "q_proj",
        "k_proj",
        "v_proj",
        "o_proj",
        "gate_proj",
        "up_proj",
        "down_proj",
    ],
)

trainer = GRPOTrainer(
    model=model,  # can also pass a loaded model object
    args=training_args,
    train_dataset=train_dataset,
    reward_funcs=reward_func,
    processing_class=tokenizer,  # tokenizer
    peft_config=peft_config,  # comment out to full-finetune (not recommended on 3060)
)

model.eval()


@torch.no_grad()
def generate_one(prompt: str, max_new_tokens: int = 256) -> str:
    model = trainer.model
    model.eval()

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    out = model.generate(
        **inputs,
        do_sample=True,
        temperature=0.8,
        top_p=0.95,
        max_new_tokens=max_new_tokens,
        pad_token_id=tokenizer.eos_token_id,
    )
    text = tokenizer.decode(out[0], skip_special_tokens=True)
    # Many models echo the prompt; trim if desired:
    if text.startswith(prompt):
        return text[len(prompt) :]
    return text


def main():
    test_prompt = train_dataset[0]["prompt"]

    print("\n=== BEFORE TRAINING ===")
    print(generate_one(test_prompt))

    print("\n=== TRAINING (GRPO) ===")
    trainer.train()

    print("\n=== AFTER TRAINING ===")
    print(generate_one(test_prompt))

    # Save adapters (LoRA) and tokenizer
    trainer.save_model("grpo_out/final")
    tokenizer.save_pretrained("grpo_out/final")


if __name__ == "__main__":
    main()
