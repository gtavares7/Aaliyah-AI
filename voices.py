import speech_recognition as sr
import pyttsx3
import time
import os
import webbrowser
import wikipedia
import pywhatkit
import pyjokes

# Engine properties
listener = sr.Recognizer()
engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
for voice in voices:
    print("Voice: %s" % voice.name)
    print(" - ID: %s" % voice.id)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    print("\n")
 