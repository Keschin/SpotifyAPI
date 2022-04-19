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
results = sp.current_user_saved_tracks()
