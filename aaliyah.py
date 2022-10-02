#
# Aaliyah
# Version: 1.0
# Created by Gabriel Tavares
#

import speech_recognition as sr
import pyttsx3
import datetime
import time
import os
import webbrowser
import wikipedia
import pywhatkit
import pyjokes

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

# main function
if __name__ == '__main__':
    clear = lambda: os.system('cls')

clear()
wishMe()
username()

while True:
    query = takeCommand().lower()

    # tell cureent time
    if 'time' in query:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        speak('Current time is' + time)
        time.sleep(5)

    # search wikipedia
    elif 'wikipedia' in query:
        speak('Searching wikipedia...')
        query = query.replace('wikipedia', '')
        results = wikipedia.summary(query, sentence = 3)
        speak('According to wikipedia')
        speak(results)
        print('results')

    # open website
    elif 'open up' in query:
        website = query.replace('open up', '')
        speak('opening up' + website)
        webbrowser.open_new_tab(website)

    # open youtube
    elif 'open youtube' in query:
        speak('Opening youtube')
        webbrowser.open_new_tab('https://youtube.com')
        time.sleep(2)

    # open Google
    elif 'open google' in query:
        speak('opening google')
        webbrowser.open_new_tab('https://www.google.ca')
        time.sleep(2)

    # play music
    elif 'play' in query:
        song = query.replace('play', '')
        speak('Playing' + song)
        pywhatkit.playonyt(song)
        time.sleep(5)

    elif 'search' in query:
        search = query.replace('search', '')
        speak('looking up' + search)
        pywhatkit.info(search, lines = 4)
        time.sleep(3)
    
    elif 'tell me a joke' in query:
        speak(pyjokes.get_joke())
        time.sleep(5)
