import spotipy
from spotipy import SpotifyOAuth

# Hier werden die Rechte und persönliche ID's vergeben
client_ID = 'ba90c35f938e41b293136e6e325c699d'
client_Secret = 'e788a1cd44e9438fbbd99bf00f923e81'
scope = 'user-top-read'
client_redireect_uri = 'http://localhost:99/callback'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Test Commit für Github Desktop Version
results = sp.current_user_saved_tracks()
