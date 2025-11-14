## Inspired from https://github.com/ni5arga/spotify-stats-python and https://spotipy.readthedocs.io/en/2.25.1/
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os


def setup_spotify_client():
    CLIENT_ID = os.environ.get("CLIENT_ID")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
    REDIRECT_URI = os.environ.get("CLIENT_REDIRECT_URI")
    SCOPE = "user-library-read user-top-read user-read-recently-played user-read-playback-state"

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope=SCOPE,
        )
    )

    return sp


if __name__ == "__main__":
    spClient = setup_spotify_client()
