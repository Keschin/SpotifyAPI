import spotipy
from spotipy import SpotifyOAuth

# Hier werden die Rechte und persönliche ID's vergeben
client_ID = 'ba90c35f938e41b293136e6e325c699d'
client_Secret = 'e788a1cd44e9438fbbd99bf00f923e81'
scope = 'user-top-read'
client_redirect_uri = 'http://localhost:99/callback'

# Hier nutzen wir die erstellten Reche und ID's für eine Authentifikation damit wir einen Token erhalten.
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id = client_ID, client_secret = client_Secret, redirect_uri = client_redirect_uri))

# Test Commit für Github Desktop Version
results = sp.current_user_saved_tracks(limit=50, offset=0, time_range='medium_term')
for song in range (50):
    list = []
    list.append(results)
    with open('top50_data.json') as f:
        data = json.load(f)
        list_of_results = data[0]["items"]
        list_of_artist_names = []
        list_of_artist_uri = []
        list_of_songs_names = []
        list_of_songs_uri = []
        list_of_durations_ms = []
        list_of_explicit = []
        list_of_albums = []
        list_of_popularity = []

        for result in list_of_results:
            result["album"]
            this_artists_name = ["artists"][0]["name"]
            list_of_artist_names.append(this_artists_name)
            this_artists_uri = result["artist"][0]["uri"]
            list_of_artists_uri.append(this_artists_uri)
            list_of_songs = result["name"]
            list_of_songs_names.append(list_of_songs)
            song_uri = result["uri"]
            list_of_song_uri.append(song_uri)
            list_of_duration = result["duration_ms"]
            list_of_durations_ms.append(list_of_duration)
            song_explicit = result["explicit"]
            list_of_explicit.append(song_explicit)
            this_album = result["album"]["name"]
            list_of_albums.append(this_album)
            song_popularity = result["popularity"]
            list_of_popularity.append(song_popularity)
        all_songs = pd.DataFrame(
            {'artist': list_of_artist_names,
             'artist_uri': list_of_artist_uri,
             'song': list_of_songs_names,
             'song_uri': list_of_songs_uri,
             'duration_ms': list_of_durations_ms,
             'explicit': list_of_explicit,
             'album': list_of_albums,
             'popularity': list_of_popularity
            })
        all_songs_saved = all_songs.to_csv('top50_songs.csv')
