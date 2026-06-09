# ''Nova AI Voice Assistant Using Python''


import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
from datetime import datetime


# TALK FUNCTION
def talk(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait() 

# RECOGNIZER
listener = sr.Recognizer()

# TAKE COMMAND
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            print("You said:", command)
            return command
    except:
        return ""

# MAIN LOGIC
def run():
    cmd = take_command()
    if not cmd:
        return

    if "youtube" in cmd:
        talk("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "google" in cmd:
        talk("Opening Google")
        webbrowser.open("https://google.com")

    elif "time" in cmd:
        time=datetime.now().strftime("Current time is %I:%M %p")
        print(time)
        talk(time)

    elif "play" in cmd:
        song = cmd.replace("play", "").strip()
        talk("Playing " + song)
        pywhatkit.playonyt(song)

    elif "search" in cmd:
        q = cmd.replace("search", "").strip()
        talk("Searching " + q)
        webbrowser.open(f"https://google.com/search?q={q}")

    elif "exit" in cmd:
        talk("Goodbye Boss")
        exit()

    else:
        talk("I did not understand")

# START
talk("Hello Boss, Nova AI is ready")

while True:
    run()













