import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
from pprint import pprint
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret_id = os.getenv("CLIENT_SECRET_ID")

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret_id)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
search_str = 'Drake'
result = sp.search(search_str, limit=1)
pprint(result)
