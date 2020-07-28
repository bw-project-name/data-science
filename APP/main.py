import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
import tekore as tk
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret_id = os.getenv("CLIENT_SECRET_ID")

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret_id)

app_token = tk.request_client_token(client_id, client_secret_id)
spotify = tk.Spotify(app_token)


def get_categories():
    all_cats = spotify.categories(limit=50)
    for cat in all_cats.items:
        print(cat.name)
        return
def get_albums():
    album = spotify.album('5abCMGtyHwpOr9cEbwfP1P')
    for track in album.tracks.items:
        print(track.track_number, track.name)
        return
def get_artist():
    artist = spotify.artist("3Y7RZ31TRPVadSFVy1o8os")
    print(artist)
    return

def get_subgenre():
    for hipster in spotify.search('tag:hipster')[0].items:
        name = hipster.name
        artist1 = hipster.artists[0].name
        print(name+ ' by '+artist1)
        print('Popularity: ', pop,'\n--')
        return

print(get_subgenre())