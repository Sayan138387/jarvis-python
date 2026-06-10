import pyttsx3
import threading

engine = pyttsx3.init()

def _speak(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    threading.Thread(
        target=_speak,
        args=(text,),
        daemon=True
    ).start()