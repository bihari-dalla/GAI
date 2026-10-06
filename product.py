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

---------------------------------------------------------------
#ollama
import ollama

prompt = f"""
Write an engaging product description for:

Product Name: {input("Product Name: ")}
Key Features: {input("Key Features: ")}
Target Audience: {input("Target Audience: ")}

Include:
1. Catchy headline
2. Persuasive description body
3. Bulleted key benefits.
"""

response = ollama.chat(
    model="llama3.2",
    messages=[{"role": "user", "content": prompt}]
)

print("\n" + "=" * 40)
print(response["message"]["content"])
