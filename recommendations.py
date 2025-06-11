import pylast
import pprint

API_KEY    = os.getenv("LASTFM_API_KEY")
API_SECRET = os.getenv("LASTFM_SECRET")
network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET)
sim = network.get_track("Radiohead", "Karma Police").get_similar(limit=2)
# extract names or MusicBrainz IDs, then search on Spotify
# print(sim)
pprint.pprint(sim)
