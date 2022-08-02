import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio) -> object:
    """

    :rtype: object
    """
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning! ")
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        print("Good Afternoon! ")
        speak("Good Afternoon. ")

    elif hour >= 18 and hour < 20:
        print("Good Evening! ")
        speak("Good Evening.")

    else:
        print('Good Night!')
        speak('Good Night.')

    speak("I am jarvis, your digit assistant...i am online and ever ready .... Please tell me how may I help you sir")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def emailSender(receiver_email, _message_):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        sender_email = 'jayden.hauff21@gmail.com'
        _password_ = 'koi357Uk'
        server.login(sender_email, _password_)
        print('Login Success')
        speak('Login Success')

        server.sendmail(sender_email, receiver_email, _message_)
        print('Your mail has been sent')
        speak('Your mail has been sent')

    except Exception:
        print('Error: Your Mail has been Failed to sent')
        speak('Sorry! The mail has failed to be sent')


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:

        query = takeCommand().lower()

        # Logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https:\\youtube.com\\chrome")
            speak("here you go")

        elif 'open meet' in query:
            webbrowser.open("https:\\meet.google.com\\chrome")
            speak("here you go")

        elif 'open classroom' in query:
            webbrowser.open("https:\\classroom.google.com\\chrome")
            speak("here you go")

        elif 'open google' in query:
            webbrowser.open("https://google.com")
            speak("here you go")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com//chrome")
            speak("here you go")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com//chrome")
            speak("here you go")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=nm#inbox")
            speak("here you go")

        elif 'open gaana' in query:
            webbrowser.open(" https: // gaana.com / newrelease// chrome")
            speak("here you go")



        elif 'play music' in query:
            music_dir = 'C:\\Users\\desktop\\Music\\Hindi'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("here you go")


        elif ' time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open visual studio ' in query:
            codePath = "C:\\Users\\desktop\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe "
            os.startfile(codePath)
            speak("here you go")

        elif 'open dev ' in query:
            devpath = "E:\\Dev-Cpp\\devcpp.exe"
            os.startfile(devpath)
            speak("here you go")

        elif 'open pycharm' in query:
            pypath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.2\\bin\\pycharm64.exe"
            os.startfile(pypath)
            speak("here you go")

        elif 'open excel' in query:
            excelpath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\EXCEL.EXE"
            os.startfile(excelpath)
            speak("here you go")

        elif 'open word' in query:
            wordpath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013"
            os.startfile(wordpath)
            speak("here you go")

        elif 'open paint' in query:
            paintpath = "C:\Windows\System32\mspaint.exe"
            os.startfile(paintpath)
            speak("here you go")

        elif 'open note plus' in query:
            notppath = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
            os.startfile(notppath)
            speak("here you go")

        elif 'open webcam' in query:
            try:
                webpath = "E:\\Iriun Webcam\\webcam.exe"
                os.startfile(webpath)
                speak("here you go")
            except Exception:
                speak('Sorry I could not find the webcam')


        elif 'open notepad' in query:
            notepath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(notepath)
            speak("here you go")

        elif "open snipping tool" in query:
            toolpath = "C:\\Windows\\System32\\SnippingTool.exe"
            os.startfile(toolpath)
            speak("here you go")

        elif 'open ward pad' in query:
            wppath = "C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe"
            os.startfile(wppath)
            speak("here you go")

        elif 'what are you doing' in query:
            speak("I Am Talking With You")



        elif 'open pdf' in query:
            pdfpath = "C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe"
            os.startfile(pdfpath)
            speak("here you go")


        elif 'open zoom' in query:
            zoompath = "C:\\Users\\desktop\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(zoompath)
            speak("here you go")

        elif 'good morning' in query:
            speak("Good morning")


        elif 'good afternoon' in query:
            speak("Good afternoon")


        elif 'good evening' in query:
            speak("Good evening")

        elif 'how are you' in query:
            speak("i am fine.. thank you sir!")

        elif 'can you laugh' in query:
            speak("yes... hahahahahahaha")

        elif 'ask me' in query:
            speak("how are you sir")

        elif 'i am fine' in query:
            speak("thank you")

        elif 'hai' in query:
            speak(" what's up")

        elif 'what is your name' in query:
            speak("jarvis")

        elif 'thanks' in query:
            speak("Your Welcome")

        elif 'thank you' in query:
            speak('Your Welcome')

        elif 'give your introduction' in query:
            speak(
                "i am jarvis.. just a random very intelligent system .. an ai which is artificial intelligence created by. srirup sarkar also known by jayden hauff")

        elif 'please exit' in query:
            speak('Activating Exit protocols...')
            speak('Good Bye')
            print('We Had a nice time! ')
            exit()
            quit()

        elif 'please leave' in query:
            speak('Activating Exit protocols...')
            speak('Good Bye')
            print('We Had a nice time! ')
            exit()
            quit()

        elif 'leave me alone' in query:
            speak('Activating Exit protocols...')
            speak('Ok sir! Good Bye')
            print('We Had a nice time! ')
            exit()
            quit()

        elif 'play joke' in query:
            speak(
                "Two men are hiking through the woods when one of them cries out, “Snake! Run!” His companion laughs at him. “Oh, relax. It’s only a baby,” he says. “Don’t you...")

        elif "mail" in query:

            speak('What\'s Your Recepient email Address')
            receiver = input('Enter The Recepient Address: ')

            speak('What Shall I say')
            message = takeCommand()
            emailSender(receiver, message)


        #
        # else:
        #     speak("Sorry I don't know. I have to learn about it")
