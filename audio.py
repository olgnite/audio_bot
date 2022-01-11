import speech_recognition
import os
import random
from pyowm import OWM


sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

commands_dict = {
    'commands': {
        'greeting': ['привет', 'приветствую'],
        'create_task': ['добавить задачу', 'создать задачу', 'заметка'],
        'weather' : ['москва','екатеринбург','пермь','сочи','самара','казань']
    }
}


def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()

        return query
    except speech_recognition.UnknownValueError:
        return "Что вы сказали ?"



def greeting():

    return 'Здравствуйте сэр!'



def create_task():

    print('Что добавим в список дел ?')

    query = listen_command()
    with open('todo-list.txt', 'a',encoding='utf-8') as file:
        file.write(f'{query}\n')

    return f'Задача {query} добавлена в todo-list'


def weather():
    query = listen_command()
    owm = OWM('KEY')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(f'{query},RU')
    w = observation.weather
    temp = w.temperature('celsius')

    return temp



def main():
    while True:
        query = listen_command()

        for k, v in commands_dict['commands'].items():
            if query in v:
                print(globals()[k]())


if __name__ == '__main__':
    main()






