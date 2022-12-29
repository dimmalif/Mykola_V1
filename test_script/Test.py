import os
import re
import webbrowser
import youtube_dl
from moviepy.editor import *
from ytmusicapi import YTMusic

download_path = 'C:/Users/Dmytro/Desktop/Mykola_V1/bin/test_script'
download_file = 'C:/Users/Dmytro/Desktop/Mykola_V1/bin/test_script/Failed.txt'

req = 'пневмослон'


# region work functions
def search_music_albums(requests):
    all_links = []
    yt = YTMusic()
    search_results_albums = yt.search(requests, filter='albums')
    ids = [search_results_albums[i]['browseId'] for i in range(len(search_results_albums))]
    albums = [yt.get_album(browseId=ids[i]) for i in range(len(ids))]

    audio_playlist_id = [i['audioPlaylistId'] for i in albums]
    first_links = f'https://music.youtube.com/watch?v=&list={audio_playlist_id[0]}'

    lst = [i for i in range(len(audio_playlist_id))]
    audio_playlist_dictionary = dict(zip(audio_playlist_id, lst))
    list_all_links = (list(audio_playlist_dictionary))
    for i in range(len(list_all_links)):
        list(audio_playlist_dictionary)
        all_links.append(f'https://music.youtube.com/watch?v=&list={list_all_links[i]}')
        print(all_links)

    return all_links


def download_albums():

    # options = {'keepvideo': False}
    youtube_dl.YoutubeDL().extract_info('https://music.youtube.com/watch?v=&list=OLAK5uy_lnuToKRbnmYa33HXUwdrVC1zFAeXMgGHE', download=True)

    # with youtube_dl.YoutubeDL(options) as ydl:
    #     ydl.download([video_info['webpage_url']])


    # def renamed():
    #     regxp = '[\w-]+[\w:]'
    #     name = []
    #
    #     result = re.findall(regxp, save_link)
    #     final_link = '\\\\'.join(result)
    #     for i in range(len(video_info['entries'])):
    #         name.append(f"{video_info['entries'][i]['title']}-{video_info['entries'][i]['id']}")
    #
    #     for i in range(len(name)):
    #         video = VideoFileClip(os.path.join(save_link, name[i] + '.mp4'))
    #         video.audio.write_audiofile(os.path.join(final_link, final_link, name[i] + '.mp3'))
    #
    # renamed()


download_albums()
# removed_algoritm
# if flag_renamed:

# endregion
