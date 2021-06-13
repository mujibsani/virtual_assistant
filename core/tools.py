import datetime
import random
import psutil
import clipboard
from . import main_common_def


def read_selected_text():
    text = clipboard.paste()
    return text


def cpu():
    usage = str(psutil.cpu_percent())
    main_common_def.speak('cpu using percentage is ' + usage)
    battery = str(psutil.sensors_battery())
    if battery == 'None':
        main_common_def.speak(' u r using it, in AC mode')
    else:
        main_common_def.speak('battery percentage is ' + battery)


def roll_dices():
    main_common_def.speak('o ok, rolling a die for you')
    die = ['1', '2', '3', '4', '5', '6']
    roll = []
    roll.extend(die)
    random.shuffle(roll)
    roll = (''.join(roll[0]))
    main_common_def.speak('I roll die and you got ' + roll)


def coin_flip():
    main_common_def.speak('flipping coin')
    coin = ['head', 'tail']
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss = (''.join(toss[0]))
    main_common_def.speak('o ok, i flipped the coin and you got : ' + toss)


def time():
    time_ = datetime.datetime.now().strftime("%I:%M:%S")
    main_common_def.speak(time_)


def date():
    day = datetime.datetime.now().day
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year

    main_common_def.speak(day)
    main_common_def.speak(month)
    main_common_def.speak(year)
