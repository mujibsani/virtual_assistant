import speech_recognition as sp_r  # voice input
from core.data_related_operations import screen_shot, remember_data, password_generator
from time import sleep
import os
import pyjokes
from nltk.tokenize import word_tokenize
from core.external_data.externalAPI import covid
from core.search_ import search_in_google, search_wiki, youtube_play
from core.tools import read_selected_text, cpu, roll_dices, coin_flip, time, date
from core.main_common_def import this_pc, speak, wish_user
from core.messaging import  send_email


def commend_from_cmd():
    query = input('how can i help you: ')
    return query


def commend_from_voice_input():
    try:
        recognizer = sp_r.Recognizer()
        with sp_r.Microphone() as source:
            print('Listening..')
            recognizer.pause_threshold = 1
            audio = recognizer.listen(source)
        try:
            print('recognizing..')
            query = recognizer.recognize_google(audio, language='en-IN')
            print(query)
        except Exception as e:
            print(e)
            speak('Audio again.')
            return None
    except :
        query = commend_from_cmd()
        return query


if __name__ == "__main__":

    wish_user()
    while True:
        # query = commend_from_cmd().lower()  # This input from textinput
        query = commend_from_voice_input().lower()

        query_for_wake = word_tokenize(query)
        print(query_for_wake)

        # query = commend_from_voice_input().lower() # This input from voice input

        wake_word = 'shahir'
        if wake_word in query_for_wake:
            if 'time' in query:
                time()
            elif 'date' in query:
                date()

            elif 'wikipedia' in query:
                search_wiki()
            elif 'search' in query or 'google' in query:
                search_in_google()
            elif 'youtube' in query:
                youtube_play()
            # elif 'open' in query:
            #     os.system('explorer C://{}'.format(query.replace()))
            elif 'open code' in query or 'vs code' in query or 'visual studio code' in query:
                code_path = f"C:\\Users\\{this_pc()}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(code_path)

            elif 'joke' in query or 'jokes' in query:
                speak(pyjokes.get_jokes())
                sleep(10)
            elif 'screenshot' in query:
                screen_shot()
            elif 'remember' in query:
                remember_data()

            elif 'password' in query:
                password_generator()
            elif 'flip' in query:
                coin_flip()
            elif 'roll' in query:
                roll_dices()
            elif 'cpu' in query:
                cpu()
            elif 'covid' in query:
                covid()
            elif 'read' in query:
                speak(read_selected_text())
            elif 'email' in query:
                email_list = {
                    'test email': 'asdfasd@gmail.com'  # use 10 minute email
                }
                try:
                    speak('To whom you want to send the mail : ')
                    name = commend_from_voice_input()
                    receiver = email_list[name]
                    speak('what is the subject of the mail')
                    subject = commend_from_voice_input()
                    speak('What should i sand: ')
                    content = commend_from_voice_input()
                    send_email(receiver, subject, content)
                    speak('email has been send')
                except:
                    speak('unable to send email')
            elif 'message' in query:
                user_name = {
                    'assist': '+8801914710393'
                }
                try:
                    speak('To whom you want to send whats app message ? ')
                    name = commend_from_voice_input()
                    phone_number = user_name[name]
                    speak('What should i sand: ')
                    content = commend_from_voice_input()
                    send_email(phone_number, content)
                    speak('Message has been send')
                except:
                    speak('unable to send message')
            elif 'how are' in query:
                speak('i am fine. and you?')

            elif 'offline' in query:
                quit()
            else:
                speak('I dont understand your question can you please asked again? ? ?')
