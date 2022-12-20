import fileinput
import os
import re
import webbrowser
import youtube_dl
from moviepy.editor import *
from ytmusicapi import YTMusic

path = 'C:/Users/Dmytro/Desktop/Mykola_V1/bin/test_script'

req = 'княZz'


class Search_music:
    """This class accepts a path to a download folder and a query (the name of a music group).
        It is possible to search for the album of the specified group using "search_music_albums" and
        open the result in the browser.
        It is the parent class for the "Download_music" class, which is currently under development"""

    # change description

    def __init__(self, requests, save_link):
        self.to_open = None
        self.top_result = None
        self.all_links = []
        self.requests = requests
        self.save_link = save_link
        self.options = {'keepvideo': False}

    def search_music_albums(self):
        self.all_links = []
        yt = YTMusic()
        search_results_albums = yt.search(self.requests,
                                          filter='albums')  # search result for request with a given filter
        ids = [search_results_albums[i]['browseId'] for i in range(len(search_results_albums))]
        albums = [yt.get_album(browseId=ids[i]) for i in range(len(ids))]  # getting a name albums
        audio_playlist_id = [i['audioPlaylistId'] for i in albums]

        # getting a link to the first album

        self.to_open = f'https://music.youtube.com/watch?v=&list={audio_playlist_id[0]}'


        # getting a link to the all albums
        lst = [i for i in range(len(audio_playlist_id))]
        audio_playlist_dictionary = dict(zip(audio_playlist_id, lst))
        for i in range(len(list(audio_playlist_dictionary))):
            self.all_links.append(f'https://music.youtube.com/watch?v=&list={list(audio_playlist_dictionary)[i]}')

    def search_top_result(self):
        yt = YTMusic()
        search_results = yt.search(self.requests)
        result = search_results[0]['videoId']
        self.top_result = f'https://music.youtube.com/watch?v={result}'
        self.to_open = self.top_result

    def browser_open(self):
        webbrowser.open(self.to_open)


# 1)перевести перевірку та реформатування у окремий клас 2) оптимізувати клас(постійно прописується схожий код
class Downloader_music(Search_music):
    def __init__(self, requests, save_link):
        super().__init__(requests, save_link)
        self.video_info = None
        self.not_found_file = None
        self.file_list = []
        self.name = []

    def check_file(self):
        for i in range(len(self.video_info['entries'])):
            self.name.append(f"{self.video_info['entries'][i]['title']}-{self.video_info['entries'][i]['id']}")

        try:
            for i in range(len(self.name)):
                f = open(f"{self.name[i]}.mp4")
                f.close()
                self.file_list.append(self.name[i])
            return False
        except FileNotFoundError:
            self.not_found_file = list(set(self.name).difference(self.file_list))
            return True

    def renamed_downloads_file(self):
        regxp = '[\w-]+[\w:]'
        result = re.findall(regxp, self.save_link)
        final_link = '\\\\'.join(result)

        for i in range(len(self.name)):
            video = VideoFileClip(os.path.join(self.save_link, self.name[i] + '.mp4'))
            video.audio.write_audiofile(os.path.join(final_link, final_link, self.name[i] + '.mp3'))
            video.close()

        return print('renamed is successful')

    def delete_mp4(self):
        print('start delete')
        for i in range(len(self.name)):
            fileinput.close()
            os.remove(f"{self.name[i]}.mp4")
            print(f"removed {self.name[i]}")

    def download_first_albums(self):
        self.search_music_albums()
        self.video_info = youtube_dl.YoutubeDL().extract_info(url=self.to_open, download=False)

        if self.check_file():
            ...
        else:
            self.renamed_downloads_file()
            return 0

        with youtube_dl.YoutubeDL(self.options) as ydl:
            ydl.download([self.video_info['webpage_url']])
        self.renamed_downloads_file()

    def download_all_albums(self):
        self.search_music_albums()
        for i in self.all_links:
            # print(f"'Download albums:'{}") НЕ В ТОПКУ!
            video_info = youtube_dl.YoutubeDL().extract_info(url=i, download=False)
            self.video_info = video_info
            with youtube_dl.YoutubeDL(self.options) as ydl:
                ydl.download([video_info['webpage_url']])
        self.renamed_downloads_file()

    # def download_top_result(self):
    #     self.search_top_result()


r = Search_music(req, path).search_music_albums()

