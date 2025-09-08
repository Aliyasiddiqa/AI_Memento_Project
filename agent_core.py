import ollama
from memento import Memory

class Agent:
    def __init__(self, model="llama3", memory=None):
        self.model = model
        self.memory = memory

    def chat(self, user_input):
        # Save user input in memory
        if self.memory:
            self.memory.add(user_input)

        # Send input to the LLM
        response = ollama.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that remembers past chats."},
                {"role": "user", "content": user_input},
            ]
        )

        return response['message']['content']
