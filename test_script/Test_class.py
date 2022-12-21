import json
from ytmusicapi import YTMusic

path = 'C:/Users/Dmytro/Desktop/Mykola_V1/bin/test_script'
#filter = 'songs'
filter = 'albums'
req = 'княZz'


class Search_music:
    """This class accepts a path to a download folder and a query (the name of a music group).
        It is possible to search for the album of the specified group using "search_music_albums" and
        open the result in the browser.
        It is the parent class for the "Download_music" class, which is currently under development"""

    # change description

    def __init__(self, requests, save_link, filter):
        self.requests = requests
        self.save_link = save_link
        self.filter = filter

    def searcher(self):
        yt = YTMusic()
        search_results = yt.search(self.requests, filter=self.filter)

        def all_albums():
            ids = [search_results[i]['browseId'] for i in range(len(search_results))]
            albums = [yt.get_album(browseId=ids[i]) for i in range(len(ids))]  # getting a name albums
            audio_playlist_id = [i['audioPlaylistId'] for i in albums]
            print(audio_playlist_id)

        def first_albums():
            ...
        method = {
            'albums': all_albums
        }

        method[self.filter]()
#    def filtering(self):



r = Search_music(req, path, filter).searcher()

