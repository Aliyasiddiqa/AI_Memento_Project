import json
import datetime
from memento import Memory

# Initialize memory
memory = Memory("memory.json")

log_file = "chat_log.txt"

with open(log_file, "a", encoding="utf-8") as log:
    log.write("\n\n--- New Chat Session: {} ---\n".format(datetime.datetime.now()))

def get_memory():
    """Load memory.json and return data as a dictionary"""
    try:
        with open("memory.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def save_memory(key, value):
    """Save new info to memory.json"""
    data = get_memory()
    data[key] = value
    with open("memory.json", "w", encoding="utf-8") as f:
        json.dump(data, f)

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("AI: Goodbye! 👋")
        break

    # Get current memory
    facts = get_memory()

    # --- Natural reply system ---
    response = ""
    if "my name is" in user_input.lower():
        # extract name
        name = user_input.split("is")[-1].strip()
        save_memory("name", name)
        response = f"Nice to meet you, {name}! I'll remember your name."
    elif "what is my name" in user_input.lower():
        if "name" in facts:
            response = f"Your name is {facts['name']}."
        else:
            response = "Hmm, I don’t know your name yet. Can you tell me?"
    else:
        response = f"You said: {user_input}"

    print("AI:", response)

    # Save to chat log
    with open(log_file, "a", encoding="utf-8") as log:
        log.write(f"You: {user_input}\n")
        log.write(f"AI: {response}\n")
















