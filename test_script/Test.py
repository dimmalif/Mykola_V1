import webbrowser
from ytmusicapi import YTMusic

req = 'дзідзьо'


def search_music(requirements):
    yt = YTMusic()
    search_results = yt.search(requirements, filter='albums')

    ids = [search_results[i]['browseId'] for i in range(len(search_results))]

    albums = [yt.get_album(browseId=ids[i]) for i in range(len(ids))]

    audio_playlist_id = [i['audioPlaylistId'] for i in albums]

    link = f'https://music.youtube.com/watch?v=&list={audio_playlist_id[0]}'

    webbrowser.open(link)


search_music(req)
