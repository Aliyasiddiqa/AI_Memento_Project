import json
from memento import Memory, Agent

# Dummy memory object for Agent
memory = Memory("memory.json")
agent = Agent(model="llama3", memory=memory)

# Load conversation memory from file
try:
    with open("memory.json", "r") as f:
        memory_data = json.load(f)  # list of [user, ai] pairs
except (FileNotFoundError, json.JSONDecodeError):
    memory_data = []

print("🤖 AI Memento Agent Ready!")
print("Type 'history' to see past chats, 'clear' to reset memory, or just chat.")
print("---------------------------------------------------------\n")

while True:
    user_input = input("You: ")

    # Show history
    if user_input.lower() == "history":
        print("\n--- Conversation History ---")
        if not memory_data:
            print("(No history yet)")
        else:
            for user, ai in memory_data:
                print(f"User: {user}")
                print(f"AI: {ai}\n")
        print("-----------------------------\n")
        continue

    # Clear memory
    if user_input.lower() == "clear":
        memory_data = []
        with open("memory.json", "w") as f:
            json.dump(memory_data, f)
        print("🧹 Memory cleared!")
        continue

    # Normal chat
    response = agent.chat(user_input)
    print("AI:", response)

    # Save conversation to memory
    memory_data.append([user_input, response])
    with open("memory.json", "w") as f:
        json.dump(memory_data, f)









