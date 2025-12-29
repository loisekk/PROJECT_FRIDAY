import os
import speech_recognition as sr
import whisper

class VoiceListener:
    def __init__(self, use_whisper=True, model_name="base"):
        self.recognizer = sr.Recognizer()
        self.use_whisper = use_whisper

        if use_whisper:
            print(f"Loading Whisper model: {model_name}")
            self.model = whisper.load_model(model_name)
        else:
            self.model = None

    def listen(self):
        """Listen to microphone input and return recognized text."""
        with sr.Microphone() as source:
            print("🎤 Listening... (speak clearly)")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        # Try Whisper first (if enabled)
        if self.use_whisper and self.model:
            try:
                print("🧠 Processing with Whisper...")
                # Save temporary audio file for Whisper
                with open("temp.wav", "wb") as f:
                    f.write(audio.get_wav_data())

                result = self.model.transcribe("temp.wav")
                text = result["text"].strip()
                os.remove("temp.wav")
                return text
            except Exception as e:
                print(f"⚠️ Whisper failed: {e}, switching to Google...")

        # Fallback: use Google Speech Recognition
        try:
            print("🌐 Processing with Google Speech Recognition...")
            text = self.recognizer.recognize_google(audio, language="en-IN")
            return text
        except sr.UnknownValueError:
            return "Sorry, I couldn’t understand your voice."
        except sr.RequestError:
            return "Network error: Could not connect to Google API."

# 👇 Main part — listener code runs from here
if __name__ == "__main__":
    listener = VoiceListener(use_whisper=True, model_name="base")

    while True:
        command = listener.listen()
        print("🗣️ You said:", command)

        if "exit" in command.lower():
            print("👋 Exiting listener.")
            break
