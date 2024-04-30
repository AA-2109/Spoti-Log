import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import os

scope = "user-read-currently-playing, user-read-playback-state"
client_ID = 'your_client_id'
client_secret = 'your_client_secret'
redirect_uri = 'http://localhost:8888'


def if_file_exists():
    file_flag = "a" if os.path.isfile("myLog.txt") else "w"
    return file_flag


def create_log_message(data):
    album_name = "Album name: " + data["item"]["album"]["name"]
    artist_name = "Artist name: " + data["item"]["artists"][0]["name"]
    track_name = "Track name: " + data["item"]["name"]
    link_to_track = "Link to track: " + data["item"]["external_urls"]["spotify"]
    link_to_album = "Link to album: " + data["item"]["album"]["external_urls"]["spotify"]
    timestamp = time.ctime(time.time())
    return (timestamp + " | " + track_name + " | " + artist_name + " | " + album_name + " | "
            + link_to_track + " | " + link_to_album)


def write_log(results, flag, debug=False):
    # Open the file in append mode ('a')
    with open('myLog.txt', flag, encoding='utf-8') as file:
        # Write some text to the file
        file.write(results + "\n")
    if debug is True:
        print("Debug print: " + results)


def main():
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(client_id=client_ID, client_secret=client_secret, scope=scope,
                                  redirect_uri=redirect_uri))
    flag = if_file_exists()
    while True:
        data = sp.currently_playing()
        if data is None:
            write_log("Finished at " + time.ctime(time.time()), flag)
            print("Not playing right now, exiting")
            return
        current_position = data["progress_ms"]
        duration_of_track = data["item"]["duration_ms"]
        log_message = create_log_message(data)
        write_log(log_message, flag)
        # additional 7 seconds to give Spotify time to update
        time_to_sleep = ((duration_of_track - current_position) / 1000) + 7
        print(f"Sleeping for: {time_to_sleep}")
        time.sleep(time_to_sleep)


if __name__ == "__main__":
    main()
