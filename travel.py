#7th travel itenary
# ============================================
# PRACTICAL 7
# Generate Travel Itinerary using GenAI
# Model: GPT-2 via Hugging Face Transformers
# ============================================

!pip install -q transformers torch

from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2"
)

place = input("Enter the travel destination: ")

prompt = f"Create a one-day travel itinerary for {place}."

result = generator(
    prompt,
    max_length=120,
    num_return_sequences=1,
    truncation=True
)

print("\nTravel Itinerary:\n")
print(result[0]["generated_text"])

---------------------------------------------------------------------------------
#model llama3.2

import ollama

destination = input("Enter a destination (eg: Tokyo, Paris, Goa): ")
duration = input("Enter number of days (eg: 3 days, 1 week): ")

prompt = f"""
Write a travel itinerary for {destination}
lasting {duration}.

Include:
1. High-level highlights
2. Day-by-day plan with key activities
3. Local food recommendations
"""

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print("\n" + "=" * 50)
print(f"Travel Itinerary for {destination}".upper())
print(response["message"]["content"])
