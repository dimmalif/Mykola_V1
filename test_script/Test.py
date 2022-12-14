import webbrowser
import youtube_dl
from ytmusicapi import YTMusic

download_path = 'C:/Users/Dmytro/Desktop/Mykola_V1/bin/test_script'
download_file = 'C:/Users/Dmytro/Desktop/Mykola_V1/bin/test_script/Failed.txt'

req = 'ThePrettyReckless'


# region trash class
# # class Work_with_music:
# #
# #     def __init__(self, path, file, requests):
# #         self.path = path
# #         self.file = file
# #         self.requests = requests
# #
# #     def search_music(self):
# #         yt = YTMusic()
# #         search_results = yt.search(requests, filter='albums')
# #
# #         ids = [search_results[i]['browseId'] for i in range(len(search_results))]
# #
# #         albums = [yt.get_album(browseId=ids[i]) for i in range(len(ids))]
# #
# #         audio_playlist_id = [i['audioPlaylistId'] for i in albums]
# #
# #         links = f'https://music.youtube.com/watch?v=&list={audio_playlist_id[0]}'
# #         webbrowser.open(links)
# #         print(links)
# #         return links
#
#
# pass


# endregion


# region work functions
def search_music_albums(requests):
    all_links = []
    yt = YTMusic()
    search_results = yt.search(requests, filter='albums')
    ids = [search_results[i]['browseId'] for i in range(len(search_results))]
    albums = [yt.get_album(browseId=ids[i]) for i in range(len(ids))]
    print(albums)
    audio_playlist_id = [i['audioPlaylistId'] for i in albums]

#region трохи говнокоду
    lst = [i for i in range(len(audio_playlist_id))]
    audio_playlist_dictionary = dict(zip(audio_playlist_id, lst))
    print(audio_playlist_dictionary)

    first_links = f'https://music.youtube.com/watch?v=&list={audio_playlist_id[0]}'

    for i in audio_playlist_dictionary:
        all_links.append(f'https://music.youtube.com/watch?v=&list={audio_playlist_dictionary[i]}')
    print(all_links)
#endregion

    webbrowser.open(first_links)
    print(first_links)
    return first_links


def run(link):
    video_info = youtube_dl.YoutubeDL().extract_info(url=link, download=False)
    filename = f"{video_info['title']}.mp3"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))


# endregion
search_music_albums(req)

# region trash download
# def download_sound(links):
#     sound_list = []
#     sound_list.append(links)
#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         ydl.download(sound_list)
#
#
# search_music(req)

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
# endregion
