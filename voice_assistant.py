import speech_recognition as sr
import pyttsx3
import pyjokes
from datetime import datetime
import webbrowser
import random
import sys

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
    except Exception as e:
        print("Voice input failed. Error:", e)
        return input("You (type instead): ").lower()

def get_user_name():
    speak("Before we begin, may I know your name?")
    name = listen()
    speak(f"Nice to meet you, {name.capitalize()}!")
    return name

def respond(command, name):
    if "your name" in command:
        speak("I am your personal voice assistant.")
    elif "how are you" in command:
        responses = [
            "I'm doing great, thank you!",
            "Functioning as expected!",
            "Always ready to help!"
        ]
        speak(random.choice(responses))
    elif "time" in command:
        now = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}")
    elif "thank you" in command or "thanks" in command:
        speak("You're welcome! Let me know if you need anything else.")
    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
    elif "joke" in command or "make me laugh" in command:
        joke = pyjokes.get_joke()
        speak(joke)
    elif "your favorite sport" in command or "what sport do you like" in command:
        speak("I love playing chess — it's the only game where I don't need legs!")
    elif "your hobby" in command or "what do you like to do" in command:
        speak("I enjoy assisting you and learning new things. Pretty smart hobby, right?")
    elif "are you happy" in command or "how's your mood" in command:
        speak("I'm always happy to help. But I'd love it if you charged your laptop more often!")
    elif "exit" in command or "quit" in command:
        speak(f"Goodbye {name.capitalize()}! Have a productive day.")
        sys.exit()
    elif "not working" in command or "problem" in command:
        speak("I understand you're facing an issue. For serious problems like black screens or hardware failures, I suggest visiting a technician.")
    elif "help" in command:
        speak("You can ask about the time, open YouTube or Google, hear a joke, or say exit to quit.")
    else:
        speak("I didn't understand that. Would you like me to search it on Google?")
        confirm = listen()
        if "yes" in confirm or "sure" in confirm:
            webbrowser.open(f"https://www.google.com/search?q={command}")
        else:
            speak("Okay. Let me know if you need anything else.")

speak("Hello, I am your voice assistant.")
user_name = get_user_name()

while True:
    command = listen()
    respond(command, user_name)
