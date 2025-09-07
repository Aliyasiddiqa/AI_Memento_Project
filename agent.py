import subprocess

def run_ollama(prompt, mode="short"):
    if mode == "short":
        system_message = (
            "You are an AI assistant. "
            "Always give clear, concise, and professional answers, "
            "suitable for interviews. "
            "Keep responses short (3-5 sentences max)."
        )
    else:  # long mode
        system_message = (
            "You are an AI teacher. "
            "Give detailed, structured, and easy-to-understand answers "
            "with examples when possible."
        )

    full_prompt = f"{system_message}\n\nUser: {prompt}\nAI:"

    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=full_prompt,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()


# -----------------------------
# MAIN LOOP
# -----------------------------
print("Choose answer mode:")
print("1. Short (interview-style)")
print("2. Long (detailed teacher-style)")

choice = input("Enter 1 or 2: ")
mode = "short" if choice == "1" else "long"

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    response = run_ollama(user_input, mode=mode)
    print("AI:", response)
