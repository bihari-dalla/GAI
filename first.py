#pip install ollama
#ollama pull llama3.2
#ollama run llama3.2
#1. WAP for the following cases using GAI pretrained model
#1A)story generator
import ollama

topic = input("Enter story topic: ")

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"Write a short story on {topic}"
        }
    ]
)

print("\nGenerated Story:\n")
print(response["message"]["content"])

--------------------------------------------------------------------------

#1b text complete
import ollama

text = input("Enter incomplete sentence: ")

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"Complete this sentence: {text}"
        }
    ]
)

print("\nCompleted Text:\n")
print(response["message"]["content"])

------------------------------------------------------------------------------------

#1c chatbot
import ollama

print("Simple Chatbot")
print("Type 'exit' to stop.\n")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": user
            }
        ]
    )

    print("Bot:", response["message"]["content"])
