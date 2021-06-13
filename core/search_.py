import webbrowser
from core.main_common_def import this_pc, speak, get_voice, greeting_wish, wish_user
import wikipedia
import pywhatkit


def search_in_google():
    speak('what should i search ?')
    search = input("what should i search ?: ")
    webbrowser.open('https://www.google.com/search?q=' + search)


def search_wiki(query):
    speak('search in wikipedia')
    query = query.replace('wikipedia', "")
    result = wikipedia.summary(query, sentences=2)
    print(result)
    speak(result)


def youtube_play():
    speak('what should i play  in youtube: ')
    topic = input('what should i play  in youtube: ??')
    pywhatkit.playonyt(topic)
