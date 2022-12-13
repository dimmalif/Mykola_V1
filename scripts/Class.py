#from arduino_control import sock
import re
import requests
import json
import random


class Function:
    def __init__(self, text_data=None):
        self.text_data = text_data

    def reject(self):  # Throw away the excess
        result_data = re.findall(r'\w+\s(\w+|\w+\s?\w+)\s?[будь ласка]*\s(.+)', self.text_data)
        return result_data


# class Arduino(Function):
#     SOCKET = sock
#
#     def __init__(self, text_data):
#         Function.__init__(self, text_data)
#
#     def detect_command(self):
#         command = self.reject()[0][0]
#         return command
#
#     def send_to_arduino(self):
#         self.SOCKET.send(f'{self.detect_command()}|{self.reject()[0][-1]}')
#         print(f'{self.detect_command()}|{self.reject()[0][-1]}')


class Tab(Function):

    def __init__(self, text_data):
        Function.__init__(self, text_data)
        self.text_data = text_data
        self.correct_request = self.reject()[0][1][7::].replace(' ', '+') if self.reject()[0][1].split()[0] == 'купити'\
            else self.reject()[0][1]

    def get_link_google(self):
        link = f'https://www.google.com/search?client=opera-gx&q={self.correct_request}'
        return link

    def get_link_youtube(self):
        link_for_parsing = requests.get(f'https://www.youtube.com/results?search_query={self.correct_request}')
        video_id = re.findall(r'watch\?v=(\S{11})', link_for_parsing.text)
        link = f'https://www.youtube.com/watch?v={video_id[0]}'
        return link

    def get_link_ekatalog(self):
        link = f'https://ek.ua/ua/ek-list.php?search_={self.correct_request}'
        return link

    @staticmethod
    def get_link_film():
        link_for_search = 'https://uaserials.pro/films/f/year=2022;2022/imdb=0;10'
        html_code = requests.get(link_for_search).text
        links_films = re.findall(r'<a class="short-img img-fit" href="(\S+)">', html_code)
        names_of_films = re.findall(r'alt="(.+)">', html_code)
        dict_of_films = tuple(zip(names_of_films, links_films))
        selected_film = random.choice(dict_of_films)
        return selected_film
