<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=200&section=header&text=PROJECT%20FRIDAY&fontSize=60&fontColor=ffffff&fontAlignY=38&desc=AI-Powered%20Voice%20Assistant&descAlignY=58&descSize=20&animation=fadeIn" width="100%"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5--Turbo-412991?style=flat-square&logo=openai&logoColor=white)](https://openai.com)
[![Flask](https://img.shields.io/badge/Flask-API-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-22c55e?style=flat-square)]()

<br/>

> *"Hey Friday — open YouTube, play heat waves, read me the news."*
> A fully local, wake-word-activated AI assistant powered by OpenAI GPT, Google Speech Recognition, and Whisper.

</div>

---

## 🧠 What is Project Friday?

**Project Friday** is a Python-based voice assistant — inspired by Iron Man's J.A.R.V.I.S. — that listens for a wake word, understands natural language commands, and responds using AI. It can open websites, play music from a personal library, read live news headlines, and handle open-ended questions using GPT-3.5-Turbo.

It also includes a **fake REST API** (Flask) with API key auth — useful for learning how backend integrations work with AI agents.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎙️ Wake Word Detection | Listens continuously for `"Friday"` or `"Jarvis"` before activating |
| 🌐 Browser Automation | Opens Google, YouTube, WhatsApp, ChatGPT, LinkedIn, and more |
| 🎵 Music Playback | Plays songs from your personal `musicLibrary.py` via YouTube |
| 📰 Live News | Fetches top 5 Indian headlines via NewsAPI |
| 🤖 GPT Fallback | Any unrecognized command is handled by GPT-3.5-Turbo |
| 🗣️ TTS Output | Text-to-speech via `pyttsx3` (offline) or `gTTS` + `pygame` (natural) |
| 🧠 Whisper Integration | Optional OpenAI Whisper STT for higher accuracy transcription |
| 🔐 Fake REST API | Flask API with API key middleware for testing agent integrations |

---

## 📁 Project Structure

```
PROJECT FRIDAY/
│
├── main.py              # Version 1 — pyttsx3 TTS, Google STT, wake word "friday"
├── main1.py             # Version 2 — gTTS + pygame TTS, wake word "friday"
├── main2.py             # Version 3 — gTTS + pygame TTS, wake word "jarvis" (clean keys)
│
├── voice_assistant.py   # Modular VoiceListener class (Whisper + Google STT fallback)
├── musicLibrary.py      # Song name → YouTube URL mapping
├── client1.py           # Minimal OpenAI API client test
│
├── fake-api.py          # Flask REST API with API key auth (products + orders)
├── test_client.py       # HTTP test client for fake-api.py
│
├── .env                 # API keys (not committed)
├── .gitignore           # Ignores .env and .venv
└── .venv/               # Virtual environment (Python 3.13)
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/loisekk/project-friday.git
cd project-friday
```

### 2. Create and activate virtual environment
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install openai SpeechRecognition pyttsx3 gTTS pygame requests flask python-dotenv openai-whisper
```

> 💡 On Windows, `PyAudio` (required by `SpeechRecognition`) may need a wheel:
> ```bash
> pip install pipwin && pipwin install pyaudio
> ```

### 4. Configure API Keys

Create a `.env` file in the root directory:
```env
API_KEY=your_newsapi_key_here
OPENAI_API_KEY=your_openai_key_here
```

Get your keys from:
- 🔑 [NewsAPI](https://newsapi.org) — free tier supports top headlines
- 🔑 [OpenAI Platform](https://platform.openai.com)

---

## 🚀 Running the Assistant

### Standard voice assistant (recommended):
```bash
python main2.py
```
Say **"Jarvis"** to activate, then speak your command.

### With Whisper STT (higher accuracy):
```bash
python voice_assistant.py
```

### Test the Fake REST API:
```bash
# Terminal 1 — start the server
python fake-api.py

# Terminal 2 — send test requests
python test_client.py
```

---

## 🗣️ Supported Commands

```
"Open Google"          → Opens google.com
"Open YouTube"         → Opens youtube.com
"Open ChatGPT"         → Opens chatgpt.com
"Play heat waves"      → Plays from musicLibrary.py
"Play attention"       → Plays from musicLibrary.py
"News"                 → Reads top 5 headlines (India)
"What is machine learning?" → GPT-3.5-Turbo answers
"Tell me a joke"       → GPT-3.5-Turbo answers
```

---

## 🎵 Music Library

Songs are stored in `musicLibrary.py` as a `name → YouTube URL` dictionary:

```python
music = {
    "heat_waves": "https://www.youtube.com/watch?v=...",
    "attention":  "https://www.youtube.com/watch?v=...",
    ...
}
```

> To add a song: copy a YouTube URL and add it to the dictionary with a lowercase key. Then say **"Play [key name]"**.

---

## 🔐 Fake REST API Reference

The Flask API at `fake-api.py` requires an `x-api-key` header on every request.

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/products` | Returns all products |
| `POST` | `/orders` | Creates a new order |

**Example request:**
```bash
curl -X GET http://127.0.0.1:5000/products \
  -H "x-api-key: my_secret_key_98765"
```

---

## 🧩 Architecture Overview

```
         🎤 Microphone Input
               │
     ┌─────────▼──────────┐
     │  Wake Word Check   │  ← "Friday" / "Jarvis"
     └─────────┬──────────┘
               │ Activated
     ┌─────────▼──────────┐
     │  Command Listener  │  ← Google STT / Whisper
     └─────────┬──────────┘
               │
     ┌─────────▼───────────────────────┐
     │       processCommand()          │
     │                                 │
     │  open X  →  webbrowser.open()  │
     │  play X  →  musicLibrary + URL │
     │  news    →  NewsAPI fetch      │
     │  other   →  GPT-3.5-Turbo      │
     └─────────────────────────────────┘
               │
         🔊 TTS Response
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.13 |
| Speech Input | `SpeechRecognition` + Google STT / OpenAI Whisper |
| Speech Output | `pyttsx3` (offline) / `gTTS` + `pygame` (online) |
| AI Brain | OpenAI GPT-3.5-Turbo |
| News | NewsAPI |
| Browser Control | `webbrowser` |
| REST API | Flask + `python-dotenv` |

---

## 📌 Roadmap

- [ ] Add memory / conversation history to GPT calls
- [ ] Integrate weather API
- [ ] Add `calendar` and `reminder` commands
- [ ] Replace musicLibrary with Spotify API
- [ ] Build a GUI dashboard with real-time transcript display
- [ ] Package as a background service (Windows startup / systemd)

---

## 👤 Author

**Yash** — AI & ML Student @ OIST (2024–2028)

[![GitHub](https://img.shields.io/badge/GitHub-loisekk-181717?style=flat-square&logo=github)](https://github.com/loisekk)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=flat-square&logo=linkedin)](https://linkedin.com)

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=120&section=footer" width="100%"/>

*"Just say the word."*

</div>
