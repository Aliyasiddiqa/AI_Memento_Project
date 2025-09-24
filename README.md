AI Memento –
Project Overview

AI Memento is an intelligent assistant that interacts with users via text and voice.
It can:

Receive text input from the user.

Convert speech to text (STT) for processing voice input.

Generate voice responses (TTS) from text.

Simulate conversation and maintain contextual memory of interactions.

This project is designed as a Python-based local assistant and can be extended for real-time multi-user interaction in the future using LiveKit.

Features

Text Interaction

User can type commands or questions in the terminal.

AI Memento responds in text.

Speech-to-Text (STT)

Users can speak commands, which are converted to text.

Allows hands-free interaction.

Text-to-Speech (TTS)

AI responds in voice, simulating a conversational assistant.

Contextual Memory

AI can remember previous interactions during the session.

Future extension can include persistent memory for long-term learning.

Agents Used

Input Agent: Handles user input (text or speech).

Processing Agent: Processes the input and decides the AI response.

Output Agent: Handles AI output (text and/or speech).

Memory Agent: Stores interaction context within the session.

Currently, memory is session-based, meaning it stores context while the program is running. It does not persist after closing the program.

Setup Instructions

Clone the repository:

git clone <your-repo-url>
cd AI_Memento_Project


Create a virtual environment:

python -m venv venv
venv\Scripts\activate   # Windows


Install dependencies:

pip install -r requirements.txt


Dependencies include:

python-dotenv – for loading environment variables

pyttsx3 (or other TTS library) – for text-to-speech

speechrecognition or STT library – for speech-to-text

Run the AI Memento mock:

python ai_memento_mock.py


Optional .env setup (if using API keys or future integration):

API_KEY=<your-api-key>

Usage Example

Text Interaction:

You: Hello
AI Memento: Sure, I can do that!

You: What is the time?
AI Memento: This is a test response from AI Memento.


Speech Interaction:

Speak into the microphone:

“Tell me a joke”


Terminal shows:

You (voice input): Tell me a joke
AI Memento: This is a test response from AI Memento.


Voice Response (TTS):

AI Memento reads its response aloud.

Future Enhancements

Multi-user chat via LiveKit.

GUI interface for easier interaction.

Persistent memory to store long-term conversations.

Image generation capability.

Integration with real-time voice/video communication.



Conclusion

The AI Memento Project demonstrates how conversational AI can be enhanced with memory to create more personalized, context-aware interactions. By combining natural language processing, persistent memory storage, and modular Python programming, this project showcases practical skills in AI development and software design.

This project is a great example of applying AI to real-world problems, such as virtual assistants, customer support, and educational tools. It not only highlights technical expertise but also the ability to design systems that learn and adapt over time.
