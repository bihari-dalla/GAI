#4 motivational quote
#colab
!pip install -q transformers torch
from transformers import pipeline

# Initialize the text generation pipeline
generator = pipeline('text-generation', model='gpt2')

# Prompt to generate a motivational quote
prompt = input("enter a prompt")

# Generate text
results = generator(prompt, max_new_tokens=30, num_return_sequences=1, temperature=0.7, do_sample=True)

print("\ngenerated text: ")
print(results[0]["generated_text"])

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
