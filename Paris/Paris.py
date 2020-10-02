import speech_recognition as sr
import webbrowser
import pyttsx3
import random
import subprocess
import os
import time
from selenium import webdriver
import datetime
import random
from playsound import playsound
#to use reminder feature create a file named reminder.txt in the file directortor Paris
engine = pyttsx3.init('sapi5')       
voices = engine.getProperty('voices')   
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 180) 



r = sr.Recognizer()


def record_audio():
    
    with sr.Microphone() as source:
        r.energy_threshold = 2500
        voice_data = ' '
  
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
        
        try:
            voice_data = r.recognize_google(audio,language="en-IN")

        except sr.UnknownValueError:
           pass
        except sr.RequestError:
           pass
        except sr.WaitTimeoutError:
           return
        voice_data=voice_data.lower()
        print(voice_data)
        return voice_data


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def process():
    i=1
    while(i==1):
        voice_data = record_audio()
        if "are you there"  in voice_data:
            speak('on duty sir')
            return
            
        if "how are you" in voice_data:
            speak('iam fine,sir')
            return
        if "add" in voice_data:
            speak("add")
            try:
                a = int(record_audio())
            except:
                speak("did not hear that")
                return
            speak("and")
            try:
                b = int(record_audio())
            except:
                speak("did not hear that")
                return
            c=a+b
            speak(c)
            return
        if "multiply" in voice_data:
            speak("multiply")
            try:
                a = int(record_audio())
            except:
                speak("did not hear that")
                return
            speak("and")
            try:
                b = int(record_audio())
            except:
                speak("did not hear that")
                return
            c=a*b
            speak(c)
            return
        if "divide" in voice_data:
            speak("divide")
            try:
                a = int(record_audio())
            except:
                speak("did not hear that")
                return
            speak("and")
            try:
                b = int(record_audio())
            except:
                speak("did not hear that")
                return
            c=a/b
            speak(c)
            return

        if "divide" in voice_data:
            speak("divide")
            try:
                a = int(record_audio())
            except:
                speak("did not hear that")
                return
            speak("and")
            try:
                b = int(record_audio())
            except:
                speak("did not hear that")
                return
            c=a/b
            speak(c)
            return
        
        if "subtract" in voice_data:
            speak("subtract")
            try:
                a = int(record_audio())
            except:
                speak("did not hear that")
                return
            speak("and")
            try:
                b = int(record_audio())
            except:
                speak("did not hear that")
                return
            c=a-b
            speak(c)
            return
        if "open steam" in voice_data:
            speak("opening...")
            subprocess.call("C:\\Program Files (x86)\\Steam\\steam.exe")
            return
        if "open google" in voice_data:
            webbrowser.get().open("www.google.com")
            return
        if "open youtube" in voice_data:
            webbrowser.get().open("www.youtube.com")
            return
        if "open twitch" in voice_data:
            webbrowser.get().open("www.twitch.com")
            return
        if "who created you" in voice_data:
            speak("Version one of Paris was made by KIRAN RAO")
            return
        if "who made you" in voice_data:
            speak("Version one of Paris was made by KIRAN RAO")
            return
        
        if "search for" in voice_data:
            a=voice_data.split()
            b=a[2:]
            seperator=','
            c=seperator.join(b)
            speak("searching for" + c)
            webbrowser.get().open("https://www.google.com/search?q="+c)
            return
        if "time" in voice_data:
            datet=datetime.datetime.now()
            a=str(datet.time())
            b=a.split(':')
            c="now its" +str(b[0])+" hours"+" and "+ str(b[1])+" minutes"
            speak(c)
            return
        if "date" in voice_data:
            datet=datetime.datetime.now()
            a=str(datet.date())
            b=a.split('-')
            c="today is" +str(b[2])+" day"+" and "+ str(b[1])+" month"
            speak(c)
            return
        if "new reminder" in voice_data:
            a=open("Reminders.txt","a")
            speak("what is the task")
            remainder=record_audio()
            a.write(remainder+"\n")
            a.close()
            return
        if "remind me" in voice_data:
            a=open("reminders.txt","r")
            i=1
            for line in a:
                speak(str(i))
                speak(str(line))
                i=i+1
            speak("that is all")
            return
        if "roll a die" in voice_data:
            speak("rolling")
            playsound("rolldice.mp3")
            l=[1,2,3,4,5,6]
            a=random.choice(l)
            speak(a)
            return
        if "toss a coin" in voice_data:
            speak("tossing")
            playsound("coinflip.mp3")
            l=["HEADS","TAILS"]
            a=random.choice(l)
            speak(a)
            return
        else:
            speak("i didnt get that")
            return
def control(voice_data):
    List_Exit=["kill it","exit","i am done","finish it","goodbye"]
    if voice_data in List_Exit:
        speak("Goodbye")
        exit()
    while "paris" in voice_data :
        List_Greet=["yes,Sir"]
        a=random.choice(List_Greet)
        speak(a)
        process()
        break
    
       
#main program

print("""
AVAIBLE COMMANDS
>>>PARIS(STATS PARIS INTO COMMAND MODE)
>>>TOSS A COIN
>>>ROLL A DIE
>>>NEW REMINDER (ADDS A REMINDER)
>>>REMINDE ME (DIISPLAYS REMAINDER)
>>>DATE
>>>TIME
>>>SEARCH FOR(REQUIRED REQUEST)
>>>ADD
>>>SUBSTRACT
>>>MULTIPLY
>>>OPEN STEAM/GOOGLE/YOUTUBE/TWITCH
>>>EXIT/GOODBYE/IAM DONE/KILL IT (EXITS PARIS)
""")
while(1): 
    voice_data = record_audio()
    control(voice_data)


     
