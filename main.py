import os
import requests

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

PAUSE_URL = "https://api.spotify.com/v1/me/player/pause"
PLAY_URL = "https://api.spotify.com/v1/me/player/play"
access_token = os.getenv("SPOTIFY_ACCESS_TOKEN")

def pause():
    response = requests.put(PAUSE_URL,
    headers={  
        'Authorization': f'Bearer {access_token}'
    })


def play():
    response = requests.put(PLAY_URL,
    headers={
        'Authorization' : f'Bearer {access_token}'
    })


play()

