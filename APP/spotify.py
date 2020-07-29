import os
from os import getenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from models import DB, user, songs
import tekore as tk
import basilica
load_dotenv()


ARTIST = ['Drake', 'Coldplay', 'Grateful Dead', 'The Rolling Stones',
          'Rush', 'Bob Segar']

client_id = os.getenv("CLIENT_ID")
client_secret_id = os.getenv("CLIENT_SECRET_ID")
basilica_key = os.getenv("BASILICA_KEY")
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret_id)
BASILICA = basilica.Connection(basilica_key)

app_token = tk.request_client_token(client_id, client_secret_id)
sp = tk.Spotify(app_token)



#def add_artist(name):
    #""" Adding artist to the database, error if not on spotify. """
    #try:
        #spotify_artist = sp.artist(name)
        #db_user = (User.query.get(spotify_artist) or
         #          User(id=spotify_artist.id, name=name))
        #DB.session.add(db_user)
    
    