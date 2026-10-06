# ============================================
# PRACTICAL 8
# Generate Interview Questions for a Job Role
# Model: Llama 3.2 via Ollama
# ============================================

import ollama

job_role = input(
    "Enter the job role "
    "(e.g. Python Developer, Data Analyst): "
)

prompt = f"""
Generate a list of 5 interview questions
for a {job_role}.

Include:
1. 2 Technical / Hard Skill questions
2. 2 Behavioural / Situational questions
3. 1 Problem-solving question
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
print(f"INTERVIEW QUESTIONS FOR: {job_role.upper()}")
print("=" * 40 + "\n")

print(response["message"]["content"])
