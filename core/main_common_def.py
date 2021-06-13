import pyttsx3
import datetime
import socket
from core.tools import time, date


engine = pyttsx3.init()
function_list = list()
voice_rate = 135


def this_pc():
    pc_name = socket.gethostname()
    if pc_name[len(pc_name) - 2:] == 'PC' or pc_name[len(pc_name) - 2:] == 'pc':
        return pc_name[:len(pc_name) - 3]
    else:
        return pc_name


def speak(audio):
    engine.setProperty('rate', voice_rate)
    engine.say(audio)
    engine.runAndWait()


def get_voice(voice):
    voices = engine.getProperty('voices')
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', voice_rate)


def greeting_wish():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak('Good Morning')
    elif 12 <= hour < 18:
        speak('Good Afternoon')
    elif 18 <= hour < 24:
        speak('Good Evening')
    else:
        speak('Good Night')


def wish_user():
    speak('welcome back ')
    greeting_wish()
    time()
    speak('How can i Help you??')
