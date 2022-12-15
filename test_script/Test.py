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
    # print(albums)
    audio_playlist_id = [i['audioPlaylistId'] for i in albums]
    first_links = f'https://music.youtube.com/watch?v=&list={audio_playlist_id[0]}'

    # region трохи говнокоду
    lst = [i for i in range(len(audio_playlist_id))]
    audio_playlist_dictionary = dict(zip(audio_playlist_id, lst))
    # print(audio_playlist_dictionary)

    for i in audio_playlist_dictionary:
        all_links.append(f'https://music.youtube.com/watch?v=&list={audio_playlist_dictionary[i]}')
    # print(all_links)
    # endregion

    # webbrowser.open(first_links)
    # print(first_links)
    return first_links


def run(link):

    flag_renamed = False
    save_link = ('C:/Users/Dmytro/Desktop/Mykola_V1/bin/test_script')

    regxp = '[\w-]+[\w:]'
    result = re.findall(regxp, save_link)
    final_link = '\\\\'.join(result)

    video_info = youtube_dl.YoutubeDL().extract_info(url=link, download=False)

    filename = f"{video_info['title']}.mp3"
    print(filename)
    options = {
        'keepvideo': False

    }

    name = []
    for i in range(len(video_info['entries'])):
        name.append(f"{video_info['entries'][i]['title']}-{video_info['entries'][i]['id']}")

    print(name)

    # with youtube_dl.YoutubeDL(options) as ydl:
    #     ydl.download([video_info['webpage_url']])

    try:
        for i in range(len(name)):
            video = VideoFileClip(os.path.join(save_link, name[i] + '.mp4'))
            video.audio.write_audiofile(os.path.join(final_link, final_link, name[i] + '.mp3'))

        #flag_renamed = True

    except OSError:
        print('track has been download,but not renamed in mp3')

    # if flag_renamed:
    #     for i in range(len(name)):
    #         os.remove(f"{name[i]}.mp4")
    #         print(f"removed {name[i]}")

run(search_music_albums(req))

# endregion
