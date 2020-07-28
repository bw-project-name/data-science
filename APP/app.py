import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
from pprint import pprint
import json
import time
import tekore as tk
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret_id = os.getenv("CLIENT_SECRET_ID")

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret_id)

app_token = tk.request_client_token(client_id, client_secret_id)
spotify = tk.Spotify(app_token)

all_cats = spotify.categories(limit=50)
for cat in all_cats.items:
    print(cat.name)