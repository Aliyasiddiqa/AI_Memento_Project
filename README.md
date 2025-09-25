🎯 AI Memento – Intelligent Assistant

💡 Project Overview

AI Memento is a Python-based intelligent assistant that interacts with users via text and voice, simulating a conversational AI.
The project demonstrates the core capabilities of AI interaction, including:

Text input processing

Speech-to-text (STT)

Text-to-speech (TTS)

Contextual memory within sessions

It is designed for entry-level AI/ML projects, but can be extended for real-time multi-user interaction, GUI interfaces, and multimedia capabilities in the future.

✨ Key Features
1. Text Interaction

Users can type queries or commands in the terminal.

AI Memento responds with meaningful text outputs.

Example:

You: Hello
AI Memento: Sure, I can do that!

2. Speech-to-Text (STT)

Users can speak to the assistant, which converts voice to text.

Enables hands-free interaction.

Example:

You (voice input): Tell me a joke
AI Memento: This is a test response from AI Memento.

3. Text-to-Speech (TTS)

AI Memento converts its text responses to voice output, making it feel like a real assistant.

Example:

You: How are you?
AI Memento (voice): This is a test response from AI Memento.

4. Contextual Memory

AI Memento remembers previous interactions within the session.

Enables context-aware responses.

Future enhancement: persistent memory for long-term conversation tracking.

🧠 Agents in AI Memento

The project is modular and uses multiple agents for handling tasks:

Agent	Function
Input Agent	Handles user input (text or voice)
Processing Agent	Analyzes input and generates AI responses
Output Agent	Outputs responses as text and/or speech
Memory Agent	Maintains session-based context for meaningful replies

⚡ Note: Currently, memory is session-based and does not persist after the program exits.

💻 Setup Instructions
Step 1: Clone the Project
git clone <your-repo-url>
cd AI_Memento_Project

Step 2: Create a Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

Step 3: Install Dependencies
pip install -r requirements.txt


Dependencies include:

python-dotenv → Loads environment variables

pyttsx3 → Text-to-Speech

speechrecognition → Speech-to-Text

pyaudio → Microphone access for voice input

Step 4: Configure Environment Variables

Create a .env file (optional for API keys or future integrations):

API_KEY=<your-api-key>

Step 5: Run the AI Memento Mock
python ai_memento_mock.py

📖 Usage Examples
Text Input
You: Hello
AI Memento: Sure, I can do that!
You: What is the time?
AI Memento: This is a test response from AI Memento.

Speech-to-Text

Speak into the microphone:

“Tell me a joke”


Terminal shows:

You (voice input): Tell me a joke
AI Memento: This is a test response from AI Memento.

Text-to-Speech

Type or speak input:

You: How are you?
AI Memento (voice): This is a test response from AI Memento.

📂 Project Structure
AI_Memento_Project/
├─ ai_memento_mock.py   # Main script for text + voice interaction
├─ requirements.txt     # Python dependencies
├─ .env                 # Environment variables / API keys
├─ assets/              # Optional folder for logs, audio, or outputs
├─ README.md            # Project documentation

🚀 Future Enhancements

Multi-user support with LiveKit for real-time chat.

GUI interface using Tkinter or PyQt for a user-friendly experience.

Persistent memory to store conversations long-term.

AI-generated images or multimedia responses.

Integration with external APIs for enhanced knowledge or tasks.
Conclusion

The AI Memento Project demonstrates how conversational AI can be enhanced with memory to create more personalized, context-aware interactions. By combining natural language processing, persistent memory storage, and modular Python programming, this project showcases practical skills in AI development and software design.

This project is a great example of applying AI to real-world problems, such as virtual assistants, customer support, and educational tools. It not only highlights technical expertise but also the ability to design systems that learn and adapt over time.
