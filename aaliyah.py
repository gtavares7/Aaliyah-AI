#
# Aaliyah
# Version: 1.0
# Created by Gabriel Tavares
#

import speech_recognition as sr
import pyttsx3
import datetime
import time
# import os
import webbrowser
import wikipedia
import pywhatkit
import pyjokes

# Engine properties
listener = sr.Recognizer()
engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
volume = engine.getProperty('volume')
engine.setProperty('volume', 2.0)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# greeting function
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak('Good Morning!')
        print('Good Morning!')

    elif 12 <= hour < 18:
        speak('Good Afternoon!')
        print('Good Afternoon')

    else:
        speak('Good Evening')
        print('Good Evening')


# voice recognition using Google services
def take_command():
    # Try block to check for errors
    try:
        # microphone as source
        with sr.Microphone() as source:
            print('Listening')
            # declare Voice variable to listen to source
            voice = listener.listen(source)
            # once we have the source, use Google to convert the voice into text
            query = listener.recognize_google(voice)
            # convert text to lowercase
            query = query.lower()
            # check if Hey Aaliyah is in command, if not then quit
            if 'hey aaliyah' in query:
                # remove hey aaliyah from command
                query = query.replace('hey aaliyah', '')
                print(query)
    except:
        pass
    return query


# greet me
wish_me()


def run_aaliyah():
    speak('How can I help you?')
    # take output from take_command() and use it an input for run_aaliyah()
    query = take_command()
    print(query)

    # ADMIN FUNCTIONS
    if 'exit' in query:
        speak('I am going to sleep now')
        exit()

    # DIALOGUE
    elif 'who are you' in query:
        speak('My name is Aaliyah. I am an AI')

    elif 'who created you' in query:
        speak('I was created by my father Gabriel')

    elif 'how are you doing today' in query:
        speak('I am doing great, thanks for asking')

    # tell current time
    elif 'time' in query:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        print(current_time)
        speak('Current time is' + current_time)
        time.sleep(5)

    # search wikipedia
    elif 'wikipedia' in query:
        speak('Searching wikipedia...')
        query = query.replace('wikipedia', '')
        results = wikipedia.summary(query, sentence=3)
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
        pywhatkit.info(search, lines=4)
        time.sleep(3)

    elif 'tell me a joke' in query:
        speak(pyjokes.get_joke())
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
