import os
os.environ['SPOTIPY_CLIENT_ID']='01d322f91fd14a5f9370e2584d1ddb22'
os.environ['SPOTIPY_CLIENT_SECRET']='0edbe89c76674f7ea4621c140980e806'
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost'

import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-read-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_playlists(limit=50)
for i, item in enumerate(results['items']):
    print("%d %s" % (i, item['name']))
# playlists = sp.current_user_playlists()

# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None


# def main():
# 	print("hello world")

# if __name__ == "__main__":
#     main()