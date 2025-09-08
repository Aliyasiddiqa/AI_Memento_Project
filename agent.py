from memento import Memory, Agent

memory = Memory("memory.json")
agent = Agent(model="llama3", memory=memory)

print("🤖 AI Memento Agent Ready!")
print("Type 'history' to see past chats, 'clear' to reset memory, or just chat.")
print("---------------------------------------------------------\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "history":
        print("\n--- Conversation History ---")
        if not memory.data:
            print("(No history yet)")
        else:
            for item in memory.data:
                print(item)
        print("-----------------------------\n")
        continue

    if user_input.lower() == "clear":
        memory.data = []
        with open("memory.json", "w") as f:
            f.write("[]")
        print("🧹 Memory cleared!")
        continue

    response = agent.chat(user_input)
    print("AI:", response)






