#
# Aaliyah
# Version: 1.0
# Created by Gabriel Tavares
#

import speech_recognition as sr
import pyttsx3
import datetime
import time

# speech-to-text using Microsoft speech (sapi5)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# greeting function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning!')
    
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon!')

    else:
        speak('Good Evening')
    
    assname = ('Aaliyah 1 point 0')
    speak('I am your AI')
    speak(assname)

# remember name
def username():
    speak('What shall I call you?')
    uname = takeCommand()
    speak('welcome')
    speak(uname)
    speak('How can I help you?')

# voice recognition using Google services
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language = 'en')
            print(f'User said: {query}\n')

        except Exception as e:
            print(e)
            print('Unable to recognize your voice.')
            return 'None'

        return query

