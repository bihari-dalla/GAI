# ============================================
# PRACTICAL 10
# Summarize a Paragraph using GenAI
# Model: Llama 3.2 via Ollama
# ============================================

import ollama

paragraph = input(
    "Enter or paste the paragraph to summarize: \n \n"
)

prompt = f"""
Summarize the following text concisely
in 2-3 key bullet points:

{paragraph}
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
print("SUMMARY")
print("=" * 40 + "\n")

print(response["message"]["content"])
