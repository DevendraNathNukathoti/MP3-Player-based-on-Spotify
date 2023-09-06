import spotipy
from spotipy.oauth2 import SpotifyOAuth
import vlc

# Initialize the Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    redirect_uri="YOUR_REDIRECT_URI",
    scope="user-library-read user-read-playback-state user-modify-playback-state"
))

# Get the user's playlists
def get_user_playlists():
    playlists = sp.current_user_playlists()
    for idx, playlist in enumerate(playlists['items']):
        print(f"{idx + 1}. {playlist['name']}")

# Select a playlist and play it
def play_playlist(playlist_index):
    playlists = sp.current_user_playlists()
    selected_playlist = playlists['items'][playlist_index - 1]
    playlist_tracks = sp.playlist_tracks(selected_playlist['id'])

    vlc_instance = vlc.Instance()
    player = vlc_instance.media_player_new()

    for track in playlist_tracks['items']:
        track_name = track['track']['name']
        track_uri = track['track']['uri']
        media = vlc_instance.media_new(track_uri)
        media.get_mrl()
        player.set_media(media)
        player.play()
        print(f"Now playing: {track_name}")
        player.event_manager().wait_playing()

# Main program loop
while True:
    print("\n1. List User Playlists")
    print("2. Play a Playlist")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        get_user_playlists()
    elif choice == '2':
        playlist_index = int(input("Enter the playlist number: "))
        play_playlist(playlist_index)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
In this code, you'll need to replace "YOUR_CLIENT_ID", "YOUR_CLIENT_SECRET", and "YOUR_REDIRECT_URI" with your own Spotify application credentials.

Keep in mind that this is a very basic example and doesn't handle all the features and complexities of a full-featured music player. Additionally, it uses the VLC media player for playback. You can customize and expand this code to meet your specific needs and requirements.





