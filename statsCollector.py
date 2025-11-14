## Inspired from https://github.com/ni5arga/spotify-stats-python and https://spotipy.readthedocs.io/en/2.25.1/
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os


def setup_spotify_client():
    SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
    SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
    SPOTIPY_REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI")
    SCOPE = "user-library-read user-top-read user-read-recently-played user-read-playback-state"

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=SPOTIPY_CLIENT_ID,
            client_secret=SPOTIPY_CLIENT_SECRET,
            redirect_uri=SPOTIPY_REDIRECT_URI,
            scope=SCOPE,
        )
    )

    return sp


if __name__ == "__main__":
    spClient = setup_spotify_client()
