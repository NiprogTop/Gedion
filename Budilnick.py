import time, datetime
import os, sys
import pyaudio
import pyttsx3
import speech_recognition as sr

# Голос
enl = pyttsx3.init()
def talk(words):
    print(words)
    enl.say(words)
    enl.runAndWait()
    enl.stop()

# Слух
def commandm():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        #print("Говори")
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        zadanie = r.recognize_google(audio, language="ru-RU").lower() #.capitalize()
        #print("Вы сказали: " + str(zadanie))
    except sr.UnknownValueError:
        # talk("I dont understande you"), language="ru-RU"
        zadanie = commandm()
    return zadanie

talk("На какое время устанавливать?")
r = commandm()
t1 = r
talk("Будильник установлен на " + str(t1))
talk("Правильно ли установлено время будильника ?")
if "нет" in commandm():
    talk("Хорошо, будильник сброшен!")
    sys.exit(0)
now = datetime.datetime.now()
if len(str(now.minute)) == 1:
    t2min = ("0" + str(now.minute))
else:
    t2min = now.minute
t2 = str(now.hour) + ":" + str(t2min)
#print(t1)
#print(t2)
while t1 != t2:
    time.sleep(30)
    now = datetime.datetime.now()
    if len(str(now.minute)) == 1:
        t2min = ("0" + str(now.minute))
    else:
        t2min = now.minute
    t2 = str(now.hour) + ":" + str(t2min)

os.startfile("SnoopDoggSweat.mp3")





