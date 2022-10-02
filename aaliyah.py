#
# Aaliyah
# Version: 1.0
# Created by Gabriel Tavares
#

import speech_recognition as sr
import pyttsx3

# speech-to-text using Microsoft speech (sapi5)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
