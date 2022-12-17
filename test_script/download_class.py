import fileinput
import os
import re
import webbrowser
import youtube_dl
from moviepy.editor import *
from ytmusicapi import YTMusic

path = 'C:/Users/Dmytro/Desktop/Mykola_V1/bin/test_script'

req = 'daron malakian'


class Search_music:

    """This class accepts a path to a download folder and a query (the name of a music group).
        It is possible to search for the album of the specified group using "search_music_albums" and
        open the result in the browser.
        It is the parent class for the "Download_music" class, which is currently under development"""

    def __init__(self, requests, save_link):
        self.requests = requests
        self.save_link = save_link
        self.options = {'keepvideo': False}

    def search_music_albums(self):
        self.all_links = []
        yt = YTMusic()
        search_results_albums = yt.search(self.requests, filter='albums')
        ids = [search_results_albums[i]['browseId'] for i in range(len(search_results_albums))]
        albums = [yt.get_album(browseId=ids[i]) for i in range(len(ids))]

        audio_playlist_id = [i['audioPlaylistId'] for i in albums]
        first_links = f'https://music.youtube.com/watch?v=&list={audio_playlist_id[0]}'
        self.first_links = first_links
        lst = [i for i in range(len(audio_playlist_id))]

        audio_playlist_dictionary = dict(zip(audio_playlist_id, lst))
        for i in range(len(list(audio_playlist_dictionary))):
            self.all_links.append(f'https://music.youtube.com/watch?v=&list={list(audio_playlist_dictionary)[i]}')

    def download_first_albums(self):
        self.search_music_albums()
        self.video_info = youtube_dl.YoutubeDL().extract_info(url=self.first_links, download=False)

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

    def renamed_downloads_file(self):
        regxp = '[\w-]+[\w:]'

        result = re.findall(regxp, self.save_link)
        final_link = '\\\\'.join(result)

        for i in range(len(self.name)):
            video = VideoFileClip(os.path.join(self.save_link, self.name[i] + '.mp4'))
            video.audio.write_audiofile(os.path.join(final_link, final_link, self.name[i] + '.mp3'))
            video.close()

        return print('renamed is successful')

    # костиль
    def open_first_link_with_first_album(self):
        webbrowser.open(self.first_links)

    def delete_mp4(self):
        print('start delete')
        for i in range(len(self.name)):
            fileinput.close()
            os.remove(f"{self.name[i]}.mp4")
            print(f"removed {self.name[i]}")

    def check_file(self):
        self.name = []
        for i in range(len(self.video_info['entries'])):
            self.name.append(f"{self.video_info['entries'][i]['title']}-{self.video_info['entries'][i]['id']}")

        try:
            self.file_list = []
            for i in range(len(self.name)):
                f = open(f"{self.name[i]}.mp4")
                f.close()
                self.file_list.append(self.name[i])
            return False
        except FileNotFoundError:
            self.not_found_file = list(set(self.name).difference(self.file_list))
            return True

# res = Work_with_music(req, path)
# res.download_first_albums()
# # res.delete_mp4()











# class Download_music(Search_music):
#     def __init__(self, requests, save_link):
#         super().__init__(requests, save_link)
#
#     def download_first_albums(self):
#         Search_music.search_music_albums(self)
#         self.video_info = youtube_dl.YoutubeDL().extract_info(url=self.first_links, download=False)
#
#         if self.check_file():
#             ...
#         else:
#             self.renamed_downloads_file()
#             return 0
#
#         with youtube_dl.YoutubeDL(self.options) as ydl:
#             ydl.download([self.video_info['webpage_url']])
#         self.renamed_downloads_file()
#
