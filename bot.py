#!/bin/python3

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import pyjokes
import sys

#pyttsx3.speak("I will speak this text")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# # engine.say("I will speak this text")

# engine.runAndWait()

# print(voices[10].id)
# for i in range (100):    
#     print(i,voices[i].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")

    speak("i am a bot. How may i help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.paused_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"you said: {query}\n")

    except Exception as e:
        print(e)
        print("say that again")
        return "None"
    return query

def sendmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com","your-password")
    server.sendmail("youremail@gmail.com",to,content)
    server.close()


if __name__ == '__main__':
    wishme()
    while True:

        query = takeCommand().lower()

        if 'hello' or 'hey' in query:
            print('hello,how can i help you')
            speak('hello,how can i help you')

        elif 'who are you' in query:
            print("i am a bot, your assistant")
            speak("i am a bot, your assistant")
        
        elif 'can you do' in query:
            print('''i can make a note,
                play songs on youtube, tell you a joke,
                search on wikipedia, tell date and time,
                find your location,
                locate area on map,
                open differnt sites like insta youtube gmail github and searches on google.
                How may i help you?''')
            speak('''i can play songs on youtube, tell you a joke,
                search on wikipedia, tell date and time,
                find your location,
                locate area on map,
                open differnt sites like insta youtube gmail github and searches on google.
                How may i help you?''')

        elif 'play' in query:
            song = query.replace('play','')
            print('playing'+song)
            speak('playing'+song)
            pywhatkit.playont(song)


        elif 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            result =  wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(result)
            speak(result)

        elif 'what is' in command:
            name = command.replace('what is ' , '')
            info = wikipedia.summary(name, 1)
            print(info)
            speak(info)

        elif 'who is ' in command:
            name = command.replace('who is' , '')
            info = wikipedia.summary(name, 1)
            print(info)
            speak(info)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open github' in query:
            webbrowser.open("github.com")
        
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'what is ' in command :
            search = 'https://www.google.com/search?q='+command
            print(' Here is what i found on google')
            speak('searching... Here is what i found')
            webbrowser.open(search)

        #elif "play music" in query:


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is {strftime}")

        elif 'time and date' or 'date and time' in query:
            today = data.today()
            time = datetime.datetime.now().strftime('%I,%M,%p')
            date = today.strftime('%B,%d,%Y')
            print("Todays's date is ",date,'current time is',time)
            speak("current time is"+ time)
            speak("and today's date is"+date)
        
        elif 'date' in query:
            today = date.today()
            print("Today's date:",today)
            date = today.strftime('%B,%d,%Y')
            print("Today's date is:"+date)
            speak(f"Today's date is {date}")

        elif 'joke' in command:
            _joke = pyjokes.get_joke()
            print(_joke)
            speak(_joke)

        elif 'locate ' in command :
            engine_talk('locating ...')
            location = command.replace('locate', '')
            if 'on map' in location :
                location= location.replace('on map',' ')
            url = 'https://google.nl/maps/place/'+location+'/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of '+location)
            speak('Here is the location of '+location)

        elif 'location of' in command :
            engine_talk('locating ...')
            location = command.replace('find location of', '')
            url = 'https://google.nl/maps/place/'+location+'/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of '+location)
            speak('Here is the location of '+location)

        elif 'bye' or 'stop' or 'exit' in command:
            print('good bye, have a nice day !!')
            speak('good bye, have a nice day !!')
            sys.exit()


        #elif

        #elif 'open code' in query:


#sudo apt install espeak ffmpeg libespeak1
