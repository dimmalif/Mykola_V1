from ytmusicapi import YTMusic
import youtube_dl

req = 'заточка'


def search_music(req):
    yt = YTMusic()
    search_results = yt.search(req ,filter='albums')
    albums = YTMusic.get_album( browseId='MPREb_L0iCMX09J83')
    print(albums)
    res = []
    for i in search_results:
        res.append(i)
        print(res)
    return


search_music(req)

