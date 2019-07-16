import speech_recognition as sr
import os
import sys
import webbrowser
import datetime
from time import strftime
import random
from fuzzywuzzy import fuzz

import pyaudio
import pyttsx3

# Импортируем ChatterBot
#from chatterbot import ChatBot
#from chatterbot.trainers import ListTrainer


# настройки
opts = {
    "alias": ('гидеон', 'гидон', 'gideon', 'гедеон', 'гербион'),
    "tbr": ('скажи', 'расскажи', 'покажи', 'сколько', 'произнеси')}
cmds = {
        "google":('загугли', 'поищи в интернете', 'пробей в интернете'),
        "ctime": ('текущее время', 'сейчас времени', 'который час'),
        "radio": ('включи музыку', 'воспроизведи радио', 'включи радио'),
        "stupid1": ('расскажи анекдот', 'рассмеши меня', 'ты знаешь анекдоты'),
        "boltavna": ('давай поговорим', 'давай поболтаем', 'давай пошалим'),
        "mail": ('напиши письмо', 'отправь письмо', 'пиши письмо'),
        "exit": ('закройся', 'выключись'),
        "obnov": ('обновись', 'обнови базы данных'),
        "budil": ('поставь будильник', 'включи будильник'),
        "vk":('откой вк', 'открой вконтакте','зайди во вконтакте'),
        "yout":('откой ютуб','зайди в ютуб'),
        "spiscont":('открой список контактов','покажи список контактов','настройки контактов'),
        "nastr":('открой настройки акаунта','покажи настройки акаунта','настройки каунта'),
        "obnovcont":('обнови список контактов','обнови контакты','обновление контактов')
    }


# Голос
enl = pyttsx3.init()
def talk(words):
    print(words)
    enl.say(words)
    enl.runAndWait()
    enl.stop()

# Слух
def command():
    #talk("a")
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говори")
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        zadanie = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали: " + zadanie)

        if  zadanie.startswith(opts["alias"]):

            for x in opts['alias']:
                zadanie = zadanie[zadanie.find(x) + 2 : ]

            #zadanie = recognize_cmd(zadanie)
            # распознаем и выполняем команду
            #execute_cmd(cmd['cmd'])
            zadanie = proverka(zadanie)

    except sr.UnknownValueError:
        # talk("I dont understande you"), language="ru-RU"
        zadanie = command()
    except sr.RequestError as e:
        talk(" Неизвестная ошибка, проверьте интернет соединение!")
        zadanie = commandm()


    return zadanie

# Чистка запросов действия
def proverka(gi):
    maxind = 0
    ima = 0
    for y, i in cmds.items():
        for x in i:
            xr = fuzz.ratio(gi , x)
            #print(x)-+
            if xr > maxind:
                maxind = xr
                ima = y
    return ima

# Слух для письма
def commandm():
    #talk("i")
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говори")
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        zadanie = r.recognize_google(audio, language="ru-RU").lower() #.capitalize()
        print("Вы сказали: " + str(zadanie))
    except sr.UnknownValueError:
        # talk("I dont understande you"), language="ru-RU"
        zadanie = commandm()
    except sr.RequestError as e:
        zadanie = commandm()
    return zadanie

# Контакты

def contactim():
    f = open('contact.txt', 'r')
    imena = f.readlines()[5::2]
    for i in range(0, len (imena)):
        imena[i] = imena[i][:-1]
    return imena

def contactem():
    f = open('contact.txt', 'r')
    ema = f.readlines()[6::2]
    for i in range(0, len (ema)):
        ema[i] = ema[i][:-1]
    return ema

# Почта
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def komy(gi):
    maxind = 0
    ima = 0
    for i in pcontactim:
        xr = fuzz.ratio(gi, i)
        # print(x)
        if xr > maxind:
            maxind = xr
            ima = pcontactim.index(i)
    return pcontactem[ima]

def send_mail():
    #doc = open('contact.txt', 'r')
    #to_login = komy(commandm())

    with open('dobav.txt', 'r') as doc:
        loginn = doc.readlines()[0:1]
        loginn = loginn[0][:-1]
    #loginn ="kapustin200001@mail.ru"
    print(loginn)

    with open('dobav.txt', 'r') as doc:
        password = doc.readlines()[1:2]
        password = password[0][:-1]
    #password = "asd123"
    print(password)

    url = "smtp.mail.ru"

    mssg = MIMEMultipart()
    talk("Кому письмо?")
    kommy = komy(commandm())
    talk("Какая тема письма? В конце текста письма скажите: Конец письма. ")
    mssg['Subject'] = commandm()
    mssg['From'] = loginn
    talk("Текст письма!")
    body = text_of_email()
    mssg.attach(MIMEText(body, 'plain', 'UTF-8'))

    server = smtplib.SMTP_SSL(url, 465)
    if loginn == "пусто":
        talk("Неверный логин! Проверьте настройки акаунта. ")
    try:
        server.login(loginn, password)
        server.sendmail(loginn, kommy, mssg.as_string())
    except:
        talk("Ошибка отправки письма! Проверьте интернет соединение или настройки акаунта.")
        makeSomething(command())
    server.quit()

# Написание письма
def text_of_email():
    myfile = " "
    wri = 1

    while wri == 1:
        predl = " " + str(commandm())
        if "конец письма" in predl.lower():
            wri = 0
            myfile = str(myfile) + " " + str("\n \n Отправленно с помощью голосового ассистента /'Gedion'  \n ")
        elif "отмена письма" in predl.lower():
            makeSomething(command())
        else:
            predl = predl.replace(" запятая", ", ")
            predl = predl.replace("с новой строки ", "\n ")
            if predl.endswith(" точка"):
                predl = predl.replace(" точка", ". ")
            elif predl.endswith(" вопрос"):
                predl = predl.replace(" вопрос" ,"? ")
            elif predl.endswith(" восклицательный знак"):
                predl = predl.replace(" восклицательный знак", "! ")
            myfile = str(myfile) + " " + str(predl.capitalize())

    print(myfile)
    return myfile

def budilnick():
    pass



''' 
# ChatterBot
chatbot = ChatBot('Gedion')     # creat the chatBot
trainer = ListTrainer(chatbot)

def boltaem(g):
    response = chatbot.get_response(g)
    if g.startswith(opts["alias"]) and ('спасибо' in g):
        makeSomething(command())
    talk(response)
    while True:
        boltaem(commandm().lower())


# Обновление диалоговой базы данных
def upload_dict():
    talk("Обновляю")
    for _file in os.listdir('diologs'):
        chats = open('diologs/' + _file, 'r').readlines()
        trainer.train(chats)  # train the bot'diologs/chats.yml'
    talk("окей")
'''

# Алгоритм программы
def makeSomething(f):
    if f == "google":
        talk("Что я должна найти?")
        zap = 'https://www.google.com/search?q=' + command()
        webbrowser.open(zap, new=1)
        talk("Гуглю")

    elif f == "ctime":
        now = datetime.datetime.now()
        talk("Сейчас " + str(now.hour) + ":" + str(now.minute))

    #elif f == "boltavna":
        #talk('Хорошо!')
        #boltaem(commandm().lower())

    elif f == "stupid1":
        te = open('anegdot/' + str(random.randint(1, 4)) + '.txt')
        talk(te.read())

    elif f == "vk":
        webbrowser.open("https://vk.com/feed", new=1)
        talk("Открыто!")

    elif f == "yout":
        webbrowser.open("https://www.youtube.com", new=1)
        talk("Открыто!")

    elif f == "mail":
        send_mail()
        talk("написал!")

    elif f == "budil":
        os.startfile("Budilnick.exe")

    elif f == "spiscont":
        os.startfile("Contact\\Contact.exe")
        talk("Открыл!")

    elif f == "nastr":
        os.startfile("Regis\\registr.exe")
        talk("Открыл!")

    elif f == "obnovcont":
        pcontactim = contactim()
        pcontactem = contactem()
        talk("Обновил")

    #elif f == "radio":
        #os.system("C:\\Users\\Putin\\Music\\SnoopDoggSweat.mp3")

    elif f == "exit":
        talk("Так точно!")
        sys.exit(0)

    #elif f == "obnov":
        #upload_dict()

    while True:
        makeSomething(command())

pcontactim = contactim()
pcontactem = contactem()
talk("Привет Мир!")
makeSomething(command())
#send_mail()







