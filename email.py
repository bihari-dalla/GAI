#5. professional email using ollama

import ollama

theme = input("Enter a theme (e.g. success): ")

prompt = f"""
Write a short formal email:

Recipient: {input("Recipient: ")}
Purpose: {input("Purpose: ")}
Details: {input("Details: ")}

Theme: {theme}
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

print("\n" + response["message"]["content"])
