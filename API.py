import json
import os
import spotipy
import spotipy as util
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

# Hier werden die Rechte und persönliche ID's vergeben
client_ID = 'ba90c35f938e41b293136e6e325c699d'
client_Secret = 'e788a1cd44e9438fbbd99bf00f923e81'
scope = 'user-top-read'
client_redirect_uri = 'http://localhost:99/callback'

# Hier nutzen wir die erstellten Reche und ID's für eine Authentifikation damit wir einen Token erhalten.
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id = client_ID, client_secret = client_Secret, redirect_uri = client_redirect_uri))

# Hier werden die TopTracks gesucht mit bestimmten Parametern. Limit wird auf 50 gesetzt für die Top 50
results = sp.current_user_top_tracks(limit=50, offset=0, time_range='medium_term')
for song in range (50):
    list = []
    list.append(results)
    with open('top50_data.json', 'w', encoding='utf-8') as f:
        json.dump(list, f, ensure_ascii=False, indent=4)



