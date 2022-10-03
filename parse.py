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

# Engine properties
listener = sr.Recognizer()
engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
volume = engine.getProperty('volume')
engine.setProperty('volume', 2.0)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# greeting function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning!')
        print('Good Morning!')
    
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon!')
        print('Good Afternoon')

    else:
        speak('Good Evening')
        print('Good Evening')


# voice recognition using Google services
def takeCommand():
    query = input()
    return query

# greet me
wishMe()

def run_aaliyah():
    speak('How can I help you?')
    # take output from takeCommand() and use it an input for run_aaliyah()
    query = takeCommand()
    
    # ADMIN FUNCTIONS
    if 'stop listening' in query:
        speak('How long shall I pause for?')
        a = int(takeCommand())
        time.sleep(a)
        print('a')

    elif 'exit' in query:
        speak('I am going to sleep now')
        exit()

    # DIALOGUE
    elif 'who are you' in query:
        speak('My name is Aaliyah. I am an AI')

    elif 'who created you' in query:
        speak('I was created by my father Gabriel')

    elif 'how are you doing today' in query:
        speak('I am doing great, thanks for asking')

    # tell cureent time
    elif 'time' in query:
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
        print(pyjokes.get_joke())
        time.sleep(5)

    else:
        speak('I am sorry, I did not get that. Please say it again')
        print('I am sorry, I did not get that. Please say it again')


# run Aaliyah in a loop
while True:
    try:
        run_aaliyah()
    except UnboundLocalError:
        print('No command detected! Shutting down')
        break