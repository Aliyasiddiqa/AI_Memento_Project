import ollama

response = ollama.chat(
    model="gemma:2b",
    messages=[
        {"role": "user", "content": "Hello, are you working now?"}
    ]
)

print("AI reply:", response["message"]["content"])
