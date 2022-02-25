import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.getenv("SPOTIFY_CLIENT_ID"),client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")))

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])

