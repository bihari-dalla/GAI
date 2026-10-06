# ============================================
# PRACTICAL 9
# Grammar Checking using GenAI
# Model: Llama 3.2 via Ollama
# ============================================

import ollama

sentence = input("Enter a sentence to check: ")

prompt = f"""
Correct the grammar, spelling, and punctuation of this sentence:

{sentence}

Provide:
1. The corrected version
2. A brief note explaining what was fixed.
"""

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\n" + "=" * 40)
print("GRAMMAR CORRECTION")
print("=" * 40 + "\n")
print(response["message"]["content"])
