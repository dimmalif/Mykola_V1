import webbrowser

import youtube_dl
from ytmusicapi import YTMusic

download_path = 'C:/Users/Dmytro/Desktop/Mykola_V1/bin/test_script'
download_file = 'C:/Users/Dmytro/Desktop/Mykola_V1/bin/test_script/Failed.txt'

req = 'ThePrettyReckless'

test_url = 'https://music.youtube.com/watch?v=XqmknZNg1yw&list=OLAK5uy_kTy5eFLo2vzxnraeFGcyOIjJRS8nx45BA'


def search_music(requests, ydl_opts=None):
    sound_list = []
    yt = YTMusic()
    search_results = yt.search(requests, filter='albums')

    ids = [search_results[i]['browseId'] for i in range(len(search_results))]

    albums = [yt.get_album(browseId=ids[i]) for i in range(len(ids))]

    audio_playlist_id = [i['audioPlaylistId'] for i in albums]

    links = f'https://music.youtube.com/watch?v=&list={audio_playlist_id[0]}'

    print('download')

    sound_list.append(links)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(sound_list)

    return links


search_music(req)
















# def download_music(links=None, ydl_opts=None):
#     sound_list = []
#     search_music(req)
#     sound_list.append(links)
#
#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         ydl.download(sound_list)
#
#
# download_music()










#     print('start')
#     search_music(requests)
#     print('searching')
#     #links = 'https://www.youtube.com/watch?v=DN1oho8kVP4&ab_channel=%D0%91%D1%8B%D1%82%D1%8C%D0%98%D0%BD%D0%B4%D0%B8%28%D0%B8%D0%BD%D0%B4%D0%B8%D0%B8%D0%B3%D1%80%D1%8B%29'
#     print('get save link')
#     save_link = ('C:/Users/Dmytro/Desktop/Mykola_V1/bin/test_script')
#     result = re.findall(save_link)
#     final_link = '\\\\'.join(result)
#     print('create name')
#     name = YouTube(links).title
#     print('Сохраняем видео...', name)
#     video_for = YouTube(links).streams.first()
#     video_for.download(final_link)
#     print('Видео сохранено... \n Конвертируем в .mp3')
#     video = VideoFileClip(os.path.join(save_link, name + '.mp4'))
#     video.audio.write_audiofile(os.path.join(final_link, final_link, name + '.mp3'))
#     return print('saved successful')


