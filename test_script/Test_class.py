import json
from ytmusicapi import YTMusic

path = 'C:/Users/Dmytro/Desktop/Mykola_V1/bin/test_script'
filter_for_search = 'top results'
#filter = None
filter = 'videos'
req = 'samurai trap'


class Search_music:
    """This class accepts a path to a download folder and a query (the name of a music group).
        It is possible to search for the album of the specified group using "search_music_albums" and
        open the result in the browser.
        It is the parent class for the "Download_music" class, which is currently under development"""

    # change description

    def __init__(self, requests, save_link, filter):
        self.top_results = None
        self.search_results = None
        self.all_links = []
        self.requests = requests
        self.save_link = save_link
        self.filter = filter
        self.yt = YTMusic()


    def all_albums(self):
        self.search_results = self.yt.search(self.requests, filter=self.filter)
        ids = [self.search_results[i]['browseId'] for i in range(len(self.search_results))]
        albums = [self.yt.get_album(browseId=ids[i]) for i in range(len(ids))]  # getting a name albums
        audio_playlist_id = [i['audioPlaylistId'] for i in albums]
        for i in range(len(audio_playlist_id)):
            self.all_links.append(f'https://music.youtube.com/watch?v=&list={audio_playlist_id[i]}')
        print(self.all_links)

    def top_result(self):
        self.search_results = self.yt.search(self.requests, filter=self.filter)
        result = self.search_results[0]['videoId']
        self.top_results = f'https://music.youtube.com/watch?v={result}'
        self.to_open = self.top_result
        print(self.top_results)

    method = {
        'albums': all_albums,
        'top result': top_result,
        'videos': top_result
    }

    def run(self):
        self.method[filter]()

#    method[self.filter]()
#    def filtering(self):

r = Search_music(req, path, filter).run()



