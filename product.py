# ============================================
# 6 . product desccription
# Generate Product Description using GenAI
# Model: GPT-2 via Hugging Face Transformers
# ============================================

!pip install -q transformers torch

from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2"
)

product = input("Enter product name: ")

prompt = f"Product: {product}\nDescription:"

result = generator(
    prompt,
    max_new_tokens=80,
    temperature=0.7,
    pad_token_id=50256
)

print("\nProduct Description:\n")
print(result[0]["generated_text"])
