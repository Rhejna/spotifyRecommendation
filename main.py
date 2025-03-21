import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="", 
                                               client_secret="",
                                               redirect_uri="http://127.0.0.1:3000/callback",
                                               scope="user-top-read"))

top_tracks = sp.current_user_top_tracks(limit=5)
recommendations = sp.recommendations(seed_tracks=[track['id'] for track in top_tracks['items']], limit=10)