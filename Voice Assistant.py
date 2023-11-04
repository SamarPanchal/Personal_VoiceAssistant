from datetime import datetime
import os as system
import speech_recognition as s
import webbrowser
import mysql.connector

recogniser = s.Recognizer()
name = "Titan"  # name for virtual assistant


def offline(val):
    while True:
        if "y" in val:
            put = input(f"You: Enter Command: ")
            if put != "":
                check(put)
                time4 = datetime.now()
                print("------" + time4.strftime("%H:%M:%S") + "------")
            else:
                exit()
        else:
            exit()


def check(query):
    if "are" in query and "you" in query:
        speak("I am your Virtual Assistant.")

    elif "what" and "can " and "do" in query:
        speak("I can Automate you Daily tasks, and can give you some Information.")

    elif "time" in query:
        time = datetime.now()
        t = time.strftime("%H:%M:%S")
        speak("Time is " + t)

    elif "what" in query and "name" in query:
        speak(f"My Name is {name}.")

    elif "hi" in query or "hello" in query or "hey" in query:
        speak("Welcome User, How Can I Help you?")

    elif "google" in query:
        speak("Opening Google...")
        webbrowser.open("https://google.com")

    elif "youtube" in query:
        speak("Opening Youtube...")
        webbrowser.open("https://youtube.com")

    elif "exit" in query or "bye" in query or "kill" in query or "close" in query:
        speak(f"Closing {name}...")
        exit()

    elif "play" in query:
        index = query.find("play")
        x = query[index + 5:]
        speak(f"Playing {x} on Youtube...")
        webbrowser.open("https://www.youtube.com/results?search_query=" + x.replace(" ", "+"))

    elif "search" in query:
        index = query.find("search")
        x = query[index + 7:]
        speak(f"Searching {x} on Google...")
        webbrowser.open("https://www.google.com/search?q=" + x.replace(" ", "+"))

    elif "invented" in query or "developed" in query:
        speak("I was Created by Samar, on 23 October at 2023 in India.")

    else:
        speak("That is not Understandable by Me.")


def speak(speech):
    system.system(f"say {speech}")
    print(f"{name}:", speech)


if __name__ == "__main__":
    time1 = datetime.now()
    if 00 <= int(time1.strftime("%H")) <= 12:
        speak(f"Good Morning User, I am your Virtual Assistant and My name is {name}.")
    elif 12 <= int(time1.strftime("%H")) <= 18:
        speak(f"Good Afternoon User, I am your Virtual Assistant and My name is {name}.")
    elif 18 <= int(time1.strftime("%H")) < 21:
        speak(f"Good Evening User, I am your Virtual Assistant and My name is {name}.")
    else:
        speak(f"May you Have a Good Sleep, I am your Virtual Assistant and My name is {name}.")
while True:
    try:
        time2 = datetime.now()
        with s.Microphone() as mic:
            print("------" + time2.strftime("%H:%M:%S") + "------")
            print(f"{name}: Listening...")
            recogniser.adjust_for_ambient_noise(mic, duration=0.1)
            voice = recogniser.listen(mic)
            speak("Recognising your Voice...")
            text = recogniser.recognize_google(voice)
            value = str(text.lower())
            print("You:", value)
            check(value)
    except Exception as e:
        if "8" in str(e):
            time2 = datetime.now()
            speak("Please Check Your Internet Connection for Voice Command!")
            print("------" + time2.strftime("%H:%M:%S") + "------")
            inp = input(f"Do You Want to Type the command for {name}? y/n: ")
            offline(inp)
        else:
            print("Error:", e)
