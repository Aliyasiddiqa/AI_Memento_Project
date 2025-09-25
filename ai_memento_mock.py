import os
from dotenv import load_dotenv
import time

# Load .env variables
load_dotenv()
LIVEKIT_URL = os.getenv("LIVEKIT_URL")

print("🔗 LiveKit URL loaded:", LIVEKIT_URL)
print("⚡ Starting AI Memento mock...")

# Simulate connecting to a room
def connect_to_room(room_name):
    print(f"✅ Connected to room: {room_name}")

# Simulate sending a message
def send_message(message):
    print(f"📤 Sending message: {message}")

# Simulate receiving a message
def receive_message():
    # Just a dummy response for testing
    responses = [
        "Hello! How can I help you?",
        "Sure, I can do that!",
        "Processing your request...",
        "This is a test response from AI Memento."
    ]
    # Pick one response
    import random
    return random.choice(responses)

# Main loop
connect_to_room("test-room")  # Replace with your room name

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("❌ Exiting AI Memento mock...")
        break

    send_message(user_input)
    time.sleep(1)  # simulate processing
    response = receive_message()
    print("AI Memento:", response)
