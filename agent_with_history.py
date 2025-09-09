import json
import os
import speech_recognition as sr
import pyttsx3
from agent_core import Agent, Memory  # make sure your Agent & Memory classes are imported

# ===== Voice helpers =====
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return ""
    except sr.RequestError as e:
        print("Could not request results; check your internet connection.", e)
        return ""

# ===== Memory & session setup =====
MEMORY_FILE = "memory.json"
CHATS_FOLDER = "chats"
os.makedirs(CHATS_FOLDER, exist_ok=True)

memory = Memory(MEMORY_FILE)
agent = Agent(model="llama3", memory=memory)

conversation_history = []

def save_session_message(user_msg, ai_msg):
    conversation_history.append({"user": user_msg, "ai": ai_msg})
    session_file = os.path.join(CHATS_FOLDER, f"chats_{len(conversation_history)}.json")
    with open(session_file, "w", encoding="utf-8") as f:
        json.dump(conversation_history, f, ensure_ascii=False, indent=2)

def list_history():
    print("Conversation history:")
    for idx, item in enumerate(conversation_history, start=1):
        print(f"{idx}. You: {item['user']}  | AI: {item['ai']}")

def reset_memory():
    memory_path = MEMORY_FILE
    if os.path.exists(memory_path):
        with open(memory_path, "w", encoding="utf-8") as f:
            f.write("{}")
        print("Memory reset successfully.")

def remove_message_from_memory_text(message_text, memory_path=MEMORY_FILE):
    if not os.path.exists(memory_path):
        with open(memory_path, "w", encoding="utf-8") as f:
            f.write("{}")
        return 0

    with open(memory_path, "r", encoding="utf-8") as f:
        content = f.read().strip()
        data = {} if not content else json.loads(content)

    removed_count = 0

    def recurse(obj):
        nonlocal removed_count
        if isinstance(obj, list):
            return [recurse(i) for i in obj if not (isinstance(i, str) and i == message_text)]
        elif isinstance(obj, dict):
            return {k: recurse(v) for k, v in obj.items() if not (isinstance(v, str) and v == message_text)}
        else:
            return obj

    new_data = recurse(data)

    with open(memory_path, "w", encoding="utf-8") as f:
        json.dump(new_data, f, ensure_ascii=False, indent=2)

    return removed_count

# ===== Main chatbot loop =====
def main():
    print("Welcome to AI Memento Day 12! Type '/exit' to quit.")

    while True:
        mode = input("Choose mode (text/voice): ").strip().lower()

        if mode == "voice":
            user_input = listen()
            print("You (voice):", user_input)
        else:
            user_input = input("You: ")

        # Commands
        if user_input.lower() in ["/exit", "/quit"]:
            print("Goodbye! 👋")
            break
        elif user_input.lower() == "/history list":
            list_history()
            continue
        elif user_input.lower() == "/reset":
            reset_memory()
            continue
        elif user_input.lower() == "/forget last":
            if conversation_history:
                last_user = conversation_history[-1]["user"]
                print("Removing last user message from memory...")
                remove_message_from_memory_text(last_user)
                print("Last user message removed.")
            else:
                print("No history to forget.")
            continue

        # Get AI response
        response = agent.chat(user_input)
        print("AI:", response)

        if mode == "voice":
            speak(response)

        save_session_message(user_input, response)

# ===== Run the chatbot =====
if __name__ == "__main__":
    main()



