# PROJECT_FRIDAY

🤖 Friday – AI Voice Assistant in Python

Friday is a Python-based AI voice assistant that integrates speech recognition, natural language processing, and system automation to deliver a hands-free intelligent user experience. Inspired by modern virtual assistants like Alexa and Google Assistant, Friday can understand voice commands, respond intelligently using OpenAI’s GPT model, automate web tasks, play music, and fetch real-time news.

This project demonstrates practical experience in AI integration, speech processing, API usage, and automation engineering.

✨ Key Features
🎙️ Voice Interaction

Wake-word activation using “Friday”

Continuous microphone listening

High-accuracy speech recognition using:

OpenAI Whisper (offline, robust)

Google Speech Recognition (online fallback)

🧠 AI Intelligence

Natural language responses powered by OpenAI GPT-3.5 Turbo

Concise, conversational replies optimized for voice output

🌐 Web Automation

Open popular platforms via voice commands:

Google

YouTube

Facebook

LinkedIn

WhatsApp

ChatGPT

🎵 Music Playback

Voice-controlled music playback

Opens predefined YouTube tracks instantly

📰 Real-Time News

Fetches and reads top headlines using NewsAPI

🔊 Text-to-Speech Output

Natural-sounding voice responses using gTTS + Pygame

Optional offline TTS support via pyttsx3

🗂️ Project Architecture
├── main.py                  # Core Friday assistant logic (wake word, commands, AI, TTS)
├── client.py                # OpenAI API test client
├── voice_assistent.py       # Advanced voice listener (Whisper + Google fallback)
├── musicLibrary.py          # Music command-to-URL mapping
├── README.md                # Project documentation

🛠️ Tech Stack

Python 3

OpenAI GPT-3.5 Turbo

SpeechRecognition

OpenAI Whisper

gTTS

Pygame

pyttsx3

NewsAPI

Webbrowser Automation

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/friday-voice-assistant.git
cd friday-voice-assistant

2️⃣ Install Dependencies
pip install speechrecognition openai gtts pygame pyttsx3 requests whisper


Note: Whisper requires FFmpeg to be installed on your system.

🔑 API Configuration
OpenAI API Key

Replace "API_KEY" in:

main.py

client.py

api_key="API_KEY"


Get your key from:
👉 https://platform.openai.com/

NewsAPI Key

Replace "API_KEY" in main.py:

newsapi = "API_KEY"


Get your key from:
👉 https://newsapi.org/

▶️ How to Run
Start the Voice Assistant
python main.py

Example Voice Commands

“Friday” → Activate assistant

“Open Google”

“Open YouTube”

“Play heat_waves”

“Tell me the news”

“What is coding?”

🎧 Whisper Voice Listener (Standalone)

Run the standalone listener to test advanced voice recognition:

python voice_assistent.py


Features:

Offline transcription using Whisper

Automatic fallback to Google Speech Recognition

Continuous listening loop

🧪 OpenAI API Test

Verify OpenAI connectivity:

python client.py

⚠️ Known Limitations

Wake-word detection is rule-based (not ML-based)

Requires active internet connection for:

OpenAI responses

Google Speech Recognition

NewsAPI

Designed primarily for desktop environments with a microphone

🚀 Future Enhancements

Machine-learning-based wake-word detection

GUI or system tray interface

Dynamic music search

Multi-language support

Noise suppression and audio enhancement

Context-aware conversation memory

👨‍💻 Author

This project was developed to explore AI-powered voice systems, real-world API integration, and intelligent automation using Python.

It highlights hands-on experience in:

AI & NLP integration

Speech recognition pipelines

API-driven application design

Desktop automation

