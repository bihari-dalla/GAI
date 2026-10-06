#4 motivational quote
#colab
!pip install -q transformers torch

from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

result = generator(
    "Write one motivational quote:",
    max_new_tokens=40,
    do_sample=True,
    temperature=0.8,
    top_p=0.9,
    repetition_penalty=1.2
)

print(result[0]["generated_text"])

-----------------------------------------------------------------------------
#ollama

import ollama

theme = input("Enter a theme: ")

prompt = f"I write a short, peaceful motivational quote about {theme}. Include an inspiring closing sentence."

response = ollama.chat(
    model="llama3.2",
    messages=[{"role": "user", "content": prompt}]
)

print("\n" + "=" * 40)
print(response["message"]["content"])
print("=" * 40)
