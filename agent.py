import pyttsx3
import speech_recognition as sr
from memento import Memory
from agent_core import Agent

memory = Memory("memory.json")
agent = Agent(model="llama3", memory=memory)
engine = pyttsx3.init()
recognizer = sr.Recognizer()

# Ask user mode
mode = input("Choose mode: (1) Voice  (2) Text\nYour choice: ")

print("✅ AI Memento Project Started")

while True:
    try:
        if mode == "1":  # Voice mode
            with sr.Microphone() as source:
                print("🎤 Speak now...")
                audio = recognizer.listen(source)
                user_input = recognizer.recognize_google(audio)
                print("You:", user_input)
        else:  # Text mode
            user_input = input("You: ")

        response = agent.chat(user_input)
        print("AI:", response)

        # Speak only in voice mode
        if mode == "1":
            engine.say(response)
            engine.runAndWait()

    except KeyboardInterrupt:
        print("\n👋 Exiting... Goodbye!")
        break

import pyttsx3
import speech_recognition as sr
from memento import Memory
from agent_core import Agent  # ✅ now imports from agent_core

def speak(text):
    """Convert text to speech"""
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("🔇 Could not speak:", e)

# Initialize
memory = Memory("memory.json")
agent = Agent(model="llama3", memory=memory)

# Setup TTS
engine = pyttsx3.init()

# Setup speech recognizer
recognizer = sr.Recognizer()
mic_available = True

try:
    sr.Microphone()
except Exception:
    mic_available = False
    print("⚠️ No microphone detected. Falling back to text mode.")

print("✅ AI Memento Project Started (Day 11 - Voice Support)")
print("🎤 Speak if mic works, or type if not.")

while True:
    try:
        if mic_available:
            # Try voice input
            with sr.Microphone() as source:
                print("🎤 Speak now (or press Ctrl+C to quit)...")
                audio = recognizer.listen(source)
                user_input = recognizer.recognize_google(audio)
                print("You:", user_input)
        else:
            # Fallback to text input
            user_input = input("You: ")

        # AI Response
        response = agent.chat(user_input)
        print("AI:", response)

        # Speak response
        speak(response)

    except sr.UnknownValueError:
        print("❌ Sorry, I didn’t understand. Try again.")
    except sr.RequestError:
        print("❌ Speech recognition service unavailable. Switching to text mode.")
        mic_available = False
    except KeyboardInterrupt:
        print("\n👋 Exiting... Goodbye!")
        break
    except Exception as e:
        print("⚠️ Error:", e)
        mic_available = False
