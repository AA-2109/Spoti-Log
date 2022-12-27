import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

black_list = "['BITZ', 'Drummatix', 'Вектор А', '43ai', 'Tony Raut', 'Oxxxymiron', 'МОЛОДОСТЬ ВНУТРИ', 'Ghostface Playa', " \
             "'Lida', 'Sagath', 'Schokk', 'IKONASTAS', 'Oxxxymiron', 'AYYO', 'bollywoodFM', 'Loqiemean', 'Neverlove', '2rbina 2rista', " \
             "'FOLKPRO', 'Oxxxymiron']"
scope = "user-read-currently-playing, user-modify-playback-state, user-read-playback-state"
my_list = []
client_ID = '4c498a92ebc0462d94fb90963c956de0'
client_secret = 'a217b14ef92d462ca315ede3a508b3b0'
redirect_uri = 'http://127.0.0.1:8080/'

sp = spotipy.Spotify(
auth_manager=SpotifyOAuth(client_id=client_ID, client_secret=client_secret, scope=scope, redirect_uri=redirect_uri))

time_in_seconds = 0
def is_in_blacklist(results):
    if results["item"]['artists'][0]['name'] in black_list:
        sp.next_track()
        time.sleep(2)
        print("BAD RUSSIAN")
    else:
        time_in_ms = results["item"]['duration_ms']
        time_in_seconds = time_in_ms / 1000.0
        print(time_in_seconds)
        sp.seek_track(0)
        time.sleep(time_in_seconds)

while True:
   results = sp.currently_playing()
   print(results["item"]['artists'][0]['name'])
   is_in_blacklist(results)


# def skip_to_next_track():
#     sp.next_track()
#
# queue = sp.queue()
# for idx, item in enumerate(queue['queue']):
#     my_list.append(item['artists'][0]['name'])
#     # time_in_seconds = (int(item['duration_ms']) / 1000.0)
#     if my_list[0] in black_list:
#         skip_to_next_track()
# print(my_list)

# track = item['track']
# print(idx, track['artists'][0]['name'], " – ", track['name'])
# print(queue['queue'][0]['artists'][0]['name'])
