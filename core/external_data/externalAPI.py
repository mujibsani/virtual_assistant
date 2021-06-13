import requests
from core import main_common_def


def covid():
    main_common_def.speak('I have 7 days ago result, ')
    covid_url = 'https://api.covidtracking.com/v1/us/daily.json'
    covid_json = requests.get(covid_url)
    covid_json = covid_json.json()
    # data = json.load(covid_json)
    covid_list = []
    for cvd in covid_json:
        covid_list.append(cvd)
    # print(len(covid_list))
    # print(covid_list[0])
    main_common_def.speak(str(covid_list[0]['positive']) + ' positive')
    main_common_def.speak(str(covid_list[0]['negative']) + ' Negative')
    # main_common_def.speak(str(covid_list[0]['pending'])+'pending')
    # main_common_def.speak(str(covid_list[0]['hospitalizedCurrently'])+' Currently hospitalized ')
    main_common_def.speak(str(covid_list[0]['inIcuCurrently'])+' Currently in Icu ')
    main_common_def.speak(str(covid_list[0]['onVentilatorCurrently'])+' Currently on Ventilator ')
    main_common_def.speak(str(covid_list[0]['death'])+' death')
    # main_common_def.speak(str(covid_list[0]['hospitalized'])+' hospitalized')
    # main_common_def.speak(str(covid_list[0]['totalTestResults'])+' total Test Results')


# def weather():
#
#     main_common_def.speak('hello')
