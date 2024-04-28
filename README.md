# Spoti-Log

This Python script uses the Spotify Web API to log the currently playing track and its details to a text file.

## Dependencies

The script uses the following  external Python libraries:
- `spotipy`

You can install these using pip:
```bash
pip install spotipy
```
## Setup

1. You need to set up a Spotify Developer Application to get your client_ID and client_secret. You can do this at the Spotify Developer Dashboard.
2. Replace 'your_client_id' and 'your_client_secret' in the script with your actual client_ID and client_secret.
3. The redirect_uri is set to 'http://localhost:8888'. Make sure this matches the redirect URI set in your Spotify Developer Application.

## Usage
Run the script with Python:
```bash
python main.py
```
The script will start logging the currently playing track and its details to a file named myLog.txt. If the file does not exist, it will be created.

## How it works

The script uses the spotipy library to authenticate with the Spotify Web API and get the currently playing track. 
It then logs the track name, artist name, album name and links to the track and album to myLog.txt.
If no track is currently playing, the script will log a “Finished” message and exit.
