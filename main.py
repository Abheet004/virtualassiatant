import win32com.client
import speech_recognition as sr
import datetime

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")   #Say that again will be printed in case of improper voice
        return "None" #None string will be returned
    return query

def speaking (text1):
    # speak the output
    speakr=win32com.client.Dispatch("SAPI.SpVoice")
    speakr.Speak(text1)

def timing():
    hour=int(datetime.datetime.now().hour)
    print(f"Time:{hour}")
    if(hour<12):
        time="Good morning"
    elif (12<hour<15):
        time="Good Afternoon"
    else:
        time="Good evening"
    return time

s= "welcome to virtual assistant"
speaking(s)
speaking(timing())
text= takeCommand()
speaking(text)