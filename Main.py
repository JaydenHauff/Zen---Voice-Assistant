import ctypes
import os
import pyttsx3
import speech_recognition as sr
import speedtest
import bs4
import requests
import wolframalpha
import Credentials
import pyjokes
import json
from urllib.request import urlopen
import webbrowser
from time import *
import timer
import pywhatkit
import pywikihow
import wikipedia
from AppOpener import run
import datetime
from rake_nltk import Rake




class Bixby_Methods :

    # # ============Speaking method
    @classmethod
    def listen(cls):
        # It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            # r.energy_threshold = 400
            r.dynamic_energy_threshold = True
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
            print(f"User said: {query}\n")  # User query will be printed.

        except Exception as e:
            # print(e)
            print("Say that again please...")  # Say that again will be printed in case of improper voice
            return "None"  # None string will be returned
        return query


    @classmethod
    def speak(cls, audio):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(audio)
        engine.runAndWait()

    # ========Taking The Command


    # ============Speed test
    @classmethod
    def runspeedTest(cls):
        speed = speedtest.Speedtest()
        d = speed.download() / 1000000  % 1000
        u = speed.upload() / 1000000   % 1000
        print(f'Download Speed : {d} \n Upload Speed : {u}')

    #          Wolframalpha
    @classmethod
    def askWolfra(cls):
        app_id = Credentials.getWolfra_Id()
        ques = input("Ask Anything : ")

        client = wolframalpha.Client(app_id)
        res = client.query(ques)
        ans = next(res.results).text
        print(ans)
        Bixby_Methods.speak(ans)

#       Jokes
    @classmethod
    def playjoke(cls):
        joke = pyjokes.get_joke()
        print(joke)
        Bixby_Methods.speak(joke)


           # Search Anything from search engine
    @classmethod
    def search_in_Google(cls):
        s = input('Enter : ')
        try:
            print("Searching...")
            sleep(3)
            pywhatkit.search(s)
        except:
            print("An unknown error occurred")


         # Lock The Device

    @classmethod
    def lock_Device(cls):
        print("locking the device")
        sleep(2)
        i=1
        while i < 2 :
            ctypes.windll.user32.LockWorkStation()
            i+=1


#       search anything on map
    @classmethod
    def gmaps(cls):
        query = input('Enter Your Search : ')
        query = query.replace("where is", "")
        location = query
        print("User asked to Locate")
        print(location)
        webbrowser.open("https://www.google.com/maps/search/" + location + "")


#       Playing anything on youtube
    @classmethod
    def play_on_Youtube(cls):
        s = input('Enter : ')
        try :
            print("Playing...")
            sleep(2)
            pywhatkit.playonyt(s)
        except:
            print("Network Error Occurred")



#        Info about a particular topic
    @classmethod
    def search_info(cls):
        search = input("Search : ")
        try:
            # print("\nSuccessfully Searched")
            # sleep(1)
            spe = wikipedia.summary(search, 1)
            pywhatkit.info(search, lines=4)
            Bixby_Methods.speak(spe + "Here are more about ")


        except:
            print("An Unknown Error Occurred")


#       Steps to prepare something
    @classmethod
    def how(cls):
        search = input("Search : ")
        max_results = 1
        how_tos = pywikihow.search_wikihow(search, 1)
        assert len(how_tos) == 1
        how_tos[0].print()

    @classmethod
    def openApp(cls):
        search = input("Search : ")
        while True:
            inp = input("Search : ").strip()
            if input:
                Bixby_Methods.speak('opening ' + search)
                run(search)

    @classmethod
    def wishMe(cls):
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            Bixby_Methods.speak("Good Morning!")

        elif hour >= 12 and hour < 18:
            Bixby_Methods.speak("Good Afternoon!")

        else:
            Bixby_Methods.speak("Good Evening!")

        Bixby_Methods.speak(" Please tell me how may I help you")

    @classmethod
    def introduction(cls):
        text = 'Hello Guys! Let me introduce myself to you all. My Name is Bixby, a voice assissant not an A.I . I have been developed by Srirup Sarkar in python programming language,' \
               'and coordinated by Soumyajeet Bhattacharya and Shloke Shinga Roy of class 10 and Section C . Though not as smart as an a.i. is but the modules which are used to build me ' \
               'up have helped me in able to answer or perform anything after a lots of days of training.  '




if __name__ == '__main__':
    Bixby_Methods.wishMe()

    while True:

        text = Bixby_Methods.listen()

        if 'introduction' in text :
            Bixby_Methods.introduction()

        elif 'open' in text :
            r = Rake()
            text = 'please can you open Adobe Photoshop CC 2023'
            r.extract_keywords_from_text(text)
            k = r.get_ranked_phrases()
            t = k[0].replace('open', '')
            Bixby_Methods.openApp(t)

        elif 'lock' in text :
            Bixby_Methods.lock_Device()

        elif 'joke' in text :
            Bixby_Methods.playjoke()

        elif 'speed test' in text:
            Bixby_Methods.runspeedTest()



