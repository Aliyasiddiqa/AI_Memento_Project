import subprocess

# Store chat history
chat_history = []

def run_ollama(prompt, mode="short"):
    """
    Run Ollama model with user prompt and memory.
    mode = "short" (interview style) or "long" (teacher style)
    """
    # Add mode instruction
    if mode == "short":
        mode_instruction = "Answer briefly, like in an interview."
    else:
        mode_instruction = "Explain in detail, like teaching a beginner."

    # Full prompt includes memory + current question
    full_prompt = "\n".join(chat_history + [f"{mode_instruction}\n{prompt}"])
    
    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=full_prompt.encode("utf-8"),
        capture_output=True
    )
    return result.stdout.decode("utf-8", errors="ignore").strip()

# --- Main Chat Loop ---
print("Choose answer mode:")
print("1. Short (Interview style)")
print("2. Long (Teacher style)")

choice = input("Enter 1 or 2: ").strip()
mode = "short" if choice == "1" else "long"

print("\n🤖 AI Memento Project (Day 3)")
print("Type 'exit' or 'quit' to stop.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye! 👋")
        break
    
    response = run_ollama(user_input, mode)
    
    # Save current question & answer to memory
    chat_history.append("You: " + user_input)
    chat_history.append("AI: " + response)
    
    print("AI:", response)
