import os
import re
import webbrowser
import youtube_dl
from moviepy.editor import *
from ytmusicapi import YTMusic

path = 'C:/Users/Dmytro/Desktop/Mykola_V1/bin/test_script'
file = 'C:/Users/Dmytro/Desktop/Mykola_V1/bin/test_script/Failed.txt'

req = 'system of a down'


class Work_with_music:
    def __init__(self, requests):
        self.requests = requests
        self.all_links = []

    def search_music_albums(self):
        yt = YTMusic()
        search_results_albums = yt.search(self.requests, filter='albums')
        ids = [search_results_albums[i]['browseId'] for i in range(len(search_results_albums))]
        albums = [yt.get_album(browseId=ids[i]) for i in range(len(ids))]

        audio_playlist_id = [i['audioPlaylistId'] for i in albums]
        first_links = f'https://music.youtube.com/watch?v=&list={audio_playlist_id[0]}'
        self.first_links = first_links
        lst = [i for i in range(len(audio_playlist_id))]

        audio_playlist_dictionary = dict(zip(audio_playlist_id, lst))
        for i in audio_playlist_dictionary:
            self.all_links.append(f'https://music.youtube.com/watch?v=&list={audio_playlist_dictionary[i]}')

        return first_links

    def download_albums(self, save_link):
        self.save_link = save_link
        self.search_music_albums()
        options = {'keepvideo': False}
        video_info = youtube_dl.YoutubeDL().extract_info(url=self.first_links, download=False)
        self.video_info = video_info
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])

        self.renamed_downloads_file()

    def renamed_downloads_file(self):
        regxp = '[\w-]+[\w:]'

        name = []
        result = re.findall(regxp, self.save_link)
        final_link = '\\\\'.join(result)

        for i in range(len(self.video_info['entries'])):
            name.append(f"{self.video_info['entries'][i]['title']}-{self.video_info['entries'][i]['id']}")

        for i in range(len(name)):
            video = VideoFileClip(os.path.join(self.save_link, name[i] + '.mp4'))
            video.audio.write_audiofile(os.path.join(final_link, final_link, name[i] + '.mp3'))
        self.name = name

        return True

    def delete_mp4(self):

        for i in range(len(self.name)):
            os.remove(f"{self.name[i]}.mp4")
            print(f"removed {self.name[i]}")


res = Work_with_music(req)
webbrowser.open(res.search_music_albums())
# print('IF:')
# if res_download:
#     res.delete_mp4()
# else: print('NOT DONE')
# Work_with_music(req).
# work = Work_with_music(req)
# link = work.search_music_albums()
# download = Work_with_music.download_albums(work, first_links=link)
