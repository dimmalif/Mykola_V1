import sys
import requests
from APIs.weather_api import API_TOKEN
import webbrowser
import subprocess
from scripts.voice import speak
from scripts.sound import Sound
from scripts.Class import Tab


def open_map_alarm(text=None):
    webbrowser.open('https://alerts.in.ua', new=2)


def buy(text=None):
    link_to_buy = Tab(text)
    webbrowser.open(link_to_buy.get_link_ekatalog())


def recommended_film(text=None):
    link_film = Tab(text)
    selected = link_film.get_link_film()
    speak(f'М+ожете перегл+янути {selected[0]}')
    webbrowser.open(selected[1])


def play_music(text=None):
    music_tab = Tab(text)
    webbrowser.open(music_tab.get_link_youtube())


def open_tabs(text=None):
    tab = Tab(text)
    webbrowser.open(tab.get_link_google())


# def send_to_arduino(text=None):
#     command = Arduino(text)
#     command.send_to_arduino()


def passive(text=None):
    pass


def volume_mute(text=None):
    Sound.mute()


def volume_m(text=None):
    Sound.volume_down()


def volume_p(text=None):
    Sound.volume_up()


def browser_y(text=None):
    webbrowser.open('https://www.youtube.com', new=2)


def weather(text=None):
    params = {"q": "Івано-Франківськ", "appid": API_TOKEN, "units": "metric", "lang": "uk"}
    response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
    w = response.json()
    speak((f"На вулиці {w['weather'][0]['description']}"))


def offBot(text=None):
    sys.exit()


def open_s(text=None):
    subprocess.Popen("C:/Steam/steam.exe")

# def writers(text=None):
#    with open('Note.txt', 'w+') as file:
#       file.write(text)
