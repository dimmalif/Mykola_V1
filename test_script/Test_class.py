import json
import os
import re

import youtube_dl
from moviepy.video.io.VideoFileClip import VideoFileClip
from ytmusicapi import YTMusic
import webbrowser

req = 'daron malakian'
path = 'C:/Users/Dmytro/Desktop/Mykola_V1/bin/test_script'

top_result = {
    'second_filter': 'top result',
    'first_filter': 'videos'
}

all_albums = {
    'second_filter': 'all albums',
    'first_filter': 'albums'
}

n = 3
n_albums = {
    'second_filter': 'n_albums',
    'first_filter': 'albums',
    'pos': n
}


class SearchMusic:
    """This class accepts a path to a download folder, and a query (the name of a music group).
        It is possible to search for the album of the specified group using “search_music_albums" and
        open the result in the browser.
        It is the parent class for the “Download_music" class, which is currently under development."""

    def __init__(self, requests, save_link, filter):
        self.result = None
        self.to_open = None
        self.top_results = None
        self.search_results = None
        self.all_links = []

        self.requests = requests
        self.save_link = save_link
        self.filter_for_functions = filter['first_filter']
        self.filter_for_method = filter['second_filter']

        self.yt = YTMusic()

        self.search_results = self.yt.search(self.requests, filter=self.filter_for_functions)
        self.position = -1 if len(filter) == 2 else filter['pos']

        self.run()

    def get_albums_links(self):
        ids = [self.search_results[i]['browseId'] for i in range(len(self.search_results))]
        albums = [self.yt.get_album(browseId=ids[i]) for i in range(len(ids))]  # getting a name albums
        audio_playlist_id = [i['audioPlaylistId'] for i in albums]

        for i in range(len(audio_playlist_id)):
            self.all_links.append(f'https://music.youtube.com/watch?v=&list={audio_playlist_id[i]}')
        self.result = self.all_links[:self.position]
        print(self.result)

    def get_top_result(self):
        result = self.search_results[0]['videoId']
        self.top_results = f'https://music.youtube.com/watch?v={result}'
        self.result = self.top_results
        print(self.result)

    def run(self):
        method = {
            'top result': self.get_top_result,
            'all albums': self.get_albums_links,
            'n_albums': self.get_albums_links
        }
        method[self.filter_for_method]()


class Work_with_files(SearchMusic):
    def __init__(self, req, path, n_albums):
        super().__init__(req, path, n_albums)
        self.not_found_file = []
        self.file_list = []
        self.name = []
        self.video_info = None
        self.isExist = []

    def download(self):
        self.video_info = youtube_dl.YoutubeDL().extract_info(url=self.result, download=False)
        with youtube_dl.YoutubeDL() as ydl:
            ydl.download([self.video_info['webpage_url']])

    def check_file(self):
        for i in range(len(self.video_info['entries'])):
            self.name.append(f"{self.video_info['entries'][i]['title']}-{self.video_info['entries'][i]['id']}")
        for i in range(len(self.name)):
            self.isExist.append(os.path.exists(f"{self.name[i]}.mp4"))

        # try:
        #     for i in range(len(self.name)):
        #         f = open(f"{self.name[i]}.mp4")
        #         f.close()
        #         self.file_list.append(self.name[i])
        #     return False
        # except FileNotFoundError:
        #     self.not_found_file = list(set(self.name).difference(self.file_list))
        #     return True
        
    def renamed_downloads_file(self):
        regxp = '[\w-]+[\w:]'
        result = re.findall(regxp, self.save_link)
        final_link = '\\\\'.join(result)

        for i in range(len(self.name)):
            video = VideoFileClip(os.path.join(self.save_link, self.name[i] + '.mp4'))
            video.audio.write_audiofile(os.path.join(final_link, final_link, self.name[i] + '.mp3'))
            video.close()

        return print('renamed is successful')


s = Work_with_files(req, path, all_albums)
s.download()
