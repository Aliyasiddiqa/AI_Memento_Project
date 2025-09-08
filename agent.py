from memento import Memory, Agent
import os
import json

memory = Memory("memory.json")

class MyAgent(Agent):
    def chat(self, user_input: str) -> str:
        clean_input = user_input.strip().lower()

        # ---- Rule: Reset memory ----
        if clean_input in ["reset memory", "clear memory", "delete memory"]:
            if os.path.exists("memory.json"):
                with open("memory.json", "w") as f:
                    f.write("[]")  # reset to empty JSON
            return "Memory has been cleared!"

        # ---- Rule: Store name ----
        if "my name is" in clean_input:
            name = user_input.split("is")[-1].strip()
            self.memory.add(f"[FACT] Your name is {name}")
            return f"Nice to meet you, {name}!"

        # ---- Rule: Recall name ----
        elif "what is my name" in clean_input:
            if os.path.exists("memory.json"):
                with open("memory.json", "r") as f:
                    try:
                        all_memory = json.load(f)
                    except:
                        all_memory = []
            else:
                all_memory = []

            facts = [m for m in all_memory if "Your name is" in m]
            if facts:
                return facts[-1].replace("[FACT] ", "")
            else:
                return "I don’t know your name yet."

        # ---- Rule: Store questions ----
        elif user_input.endswith("?"):
            self.memory.add(f"[QUESTION] {user_input}")
            return f"I’ll remember that question: {user_input}"

        # ---- Rule: Recall past questions ----
        elif "what questions did i ask" in clean_input:
            if os.path.exists("memory.json"):
                with open("memory.json", "r") as f:
                    try:
                        all_memory = json.load(f)
                    except:
                        all_memory = []
            else:
                all_memory = []

            questions = [m.replace("[QUESTION] ", "") for m in all_memory if m.startswith("[QUESTION]")]
            if questions:
                return "Here are the questions you asked:\n- " + "\n- ".join(questions)
            else:
                return "You haven’t asked me any questions yet."

        # ---- Default: store conversation ----
        else:
            self.memory.add(f"[CONVO] {user_input}")
            return f"I remember you said: {user_input}"

agent = MyAgent(model="llama3", memory=memory)

while True:
    user_input = input("You: ")
    response = agent.chat(user_input)
    print("AI:", response)


