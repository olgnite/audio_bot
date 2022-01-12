import speech_recognition
import os
import random
import webbrowser
from pyowm import OWM

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

commands_dict = {
    'commands': {
        'greeting': ['привет', 'приветствую'],
        'create_task': ['добавить задачу', 'создать задачу', 'заметка'],
        'weather': ['москва', 'екатеринбург', 'пермь', 'сочи', 'самара', 'казань'],
        'open_browser': ['вконтакте', 'видео', ]
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


def add_task(query: str):
    with open('todo-list.txt', 'a', encoding='utf-8') as file:
        file.write(f'{query}\n')


def show_text(input_arg):
    def the_real_decorator(function):
        def wrapper():
            print(input_arg)
            return function()

        return wrapper

    return the_real_decorator


@show_text("Что добавим в список дел?")
def create_task():
    query = listen_command()
    add_task(query)

    return f'Задача {query} добавлена в todo-list'


def get_weather():
    query = listen_command()
    owm = OWM('KEY')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(f'{query},RU')
    w = observation.weather
    temp = w.temperature('celsius')

    return [f'Температура в городе {query} = {temp}']


def open_browser():
    query = listen_command()
    if query == 'вконтакте':
        webbrowser.open('https://vk.com/im', new=2)
    elif query == 'видео':
        webbrowser.open('https://www.youtube.com/', new=2)
    else:
        return 'Ошибка!'


def main():
    while True:
        query = listen_command()

        for k, v in commands_dict['commands'].items():
            if query in v:
                print(globals()[k]())


if __name__ == '__main__':
    main()
