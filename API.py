import spotipy
from spotipy import SpotifyOAuth

# Hier werden die Rechte und persönliche ID's vergeben
scope = "user-library-read"
Client_ID = 'ba90c35f938e41b293136e6e325c699d'
Client_Secret = 'e788a1cd44e9438fbbd99bf00f923e81'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Test Commit für Github Desktop Version
results = sp.current_user_saved_tracks()
