import speech_recognition as sr
import pyaudio
import os


def listen():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        # r.energy_threshold = 400
        r.dynamic_energy_threshold = True
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.
        return query


    except Exception as e:
        # print(e)
        #print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned


while True :
    text = listen()

    if 'hey google' in text :
        os.popen("python Main.py")


