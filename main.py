import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=, 
                                               client_secret=,
                                               redirect_uri="http://127.0.0.1:3000/callback",
                                               scope="user-top-read,user-modify-playback-state"))

#pprint.pprint(sp.current_user_top_tracks(limit=1))
top_track = sp.current_user_top_tracks(limit=2)
print(f'Current top artist : {top_track["items"][0]["album"]["artists"][0]["name"]}, Second top artist : {top_track["items"][1]["album"]["artists"][0]["name"]}'
      f'\nCurrent top song : {top_track["items"][0]["name"]}, Second top song : {top_track["items"][1]["name"]}')

recommendations = sp.recommendations(
    seed_tracks=["0c6xIDDpzE81m2q797ordA"], 
    limit=20)
#print(recommendations['tracks'][0]['name'])
print(recommendations)