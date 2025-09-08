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

def reset_memory():
    """Clear memory.json"""
    with open("memory.json", "w", encoding="utf-8") as f:
        json.dump({}, f)

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("AI: Goodbye! 👋")
        break

    if user_input.lower() in ["reset", "clear memory"]:
        reset_memory()
        print("AI: Memory has been cleared 🧹")
        continue

    facts = get_memory()
    response = ""

    # --- Learning Facts ---
    if "my name is" in user_input.lower():
        name = user_input.split("is")[-1].strip()
        save_memory("name", name)
        response = f"Got it, your name is {name}. I'll remember that."
    elif "my age is" in user_input.lower():
        age = user_input.split("is")[-1].strip()
        save_memory("age", age)
        response = f"Thanks! I'll remember that you are {age} years old."
    elif "i live in" in user_input.lower():
        city = user_input.split("in")[-1].strip()
        save_memory("city", city)
        response = f"Great! I'll remember that you live in {city}."
    elif "my hobby is" in user_input.lower():
        hobby = user_input.split("is")[-1].strip()
        save_memory("hobby", hobby)
        response = f"Cool! I'll remember that your hobby is {hobby}."

    # --- Answering Questions ---
    elif "what is my name" in user_input.lower():
        response = f"Your name is {facts['name']}." if "name" in facts else "I don’t know your name yet."
    elif "what is my age" in user_input.lower():
        response = f"You are {facts['age']} years old." if "age" in facts else "I don’t know your age yet."
    elif "where do i live" in user_input.lower():
        response = f"You live in {facts['city']}." if "city" in facts else "I don’t know where you live yet."
    elif "what is my hobby" in user_input.lower():
        response = f"Your hobby is {facts['hobby']}." if "hobby" in facts else "I don’t know your hobby yet."
    else:
        response = f"You said: {user_input}"

    print("AI:", response)

    with open(log_file, "a", encoding="utf-8") as log:
        log.write(f"You: {user_input}\n")
        log.write(f"AI: {response}\n")

















