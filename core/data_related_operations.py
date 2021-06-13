import pyautogui
import os
import time as tt
import string
import random

from core.main_common_def import speak


def password_generator():
    string_one = string.ascii_uppercase
    string_two = string.ascii_lowercase
    string_three = string.digits
    string_four = string.punctuation

    password_len = 8
    string_list = []
    string_list.extend(list(string_one))
    string_list.extend(list(string_two))
    string_list.extend(list(string_three))
    string_list.extend(list(string_four))
    random.shuffle(string_list)
    new_pass = ("".join(string_list[0:password_len]))
    print(new_pass)
    speak(new_pass)


def remember_data():
    speak('what shoud i remember: ')
    data = input('what shoud i remember: ')
    speak('you said me to remember that ' + data)
    if os.path.exists('utils'):
        if os.path.exists("utils\\data.txt"):
            with open("utils\\data.txt", "r+") as file:
                old_data = file.read()
                file.write('\n' + data)
                file.close()
        else:
            with open("utils\\data.txt", "w") as file:
                file.write(data)
                file.close()
    else:
        os.mkdir('utils')
        with open("utils\\data.txt", "w") as file:
            file.write(data)
            file.close()
    speak('Data store completed')


def screen_shot():
    m_time = tt.time()
    if os.path.exists('screen_shot'):
        name_img = f'screen_shot\\{m_time}.png'
    else:
        os.makedirs('screen_shot')
        name_img = f'screen_shot\\{m_time}.png'
    img = pyautogui.screenshot(name_img)
    img.show()


