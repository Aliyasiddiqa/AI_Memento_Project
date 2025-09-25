from fastapi import FastAPI
from pydantic import BaseModel
from agent_core import Agent, Memory
from dotenv import load_dotenv
import os
import pyttsx3

load_dotenv()

app = FastAPI(title="AI Memento API")

# AI Memento core
memory = Memory("memory.json")
agent = Agent(model="llama3", memory=memory)

# Optional local TTS
speaker = pyttsx3.init()

class Message(BaseModel):
    text: str

@app.post("/chat")
def chat(message: Message):
    user_input = message.text
    response = agent.chat(user_input)
    speaker.say(response)
    speaker.runAndWait()
    return {"response": response}


