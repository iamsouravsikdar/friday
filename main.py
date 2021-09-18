import pyttsx3
import datetime
import speech_recognition as sr



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour

    if hour>=0 and  hour<12:
        speak("Good Morning Sir")
        print("Good Morning Sir")

    if hour>=12 and  hour<5:
        speak("Good Afternoon Sir")
        print("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")
        print("Good Evening Sir")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"master said:{statement}\n")

        except Exception as e:
            speak("Pardon me Sir, please say that again")
            return "None"
        return statement
while True:
    statement = takeCommand().lower()
    if statement == 0:
        continue
    if "initiate" in statement or "initiate friday" in statement:
        print("Loading FRIDAY")
        speak("Loading FRIDAY")
        wishMe()
        continue





