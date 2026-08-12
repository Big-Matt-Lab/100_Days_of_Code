import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "f7c85d930f6645da9fc313f16ea64ec4"
CLIENT_SECRET = "fb836324923d4097a4968c13272f5859"
REDIRECT_URI = "https://example.com"
SPOTIFY_DISPLAY_NAME = "Big.Matt.Lab"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        # username=YOUR SPOTIFY DISPLAY NAME,
    )
)
user_id = sp.current_user()["id"]