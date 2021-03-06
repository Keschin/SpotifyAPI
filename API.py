import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import img2pdf
from PIL import Image
import spotipy
import spotipy as util
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
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
# Jeder Track wird in eine Liste gepackt bzw angehängt (Append) Danach wird diese Liste mittels Json-Datei geöffnet
for song in range (50):
    list = []
    list.append(results)
    with open('top50_data.json') as f:
        data = json.load(f)
        list_of_results = data[0]["items"]
        list_of_artist_names = []
        list_of_artist_uri = []
        list_of_song_names = []
        list_of_song_uri = []
        list_of_durations_ms = []
        list_of_explicit = []
        list_of_albums = []
        list_of_popularity = []

# Hier werden die Daten noch in ein CSV gespeichert
        for result in list_of_results:
            result["album"]
            this_artists_name = result["artists"][0]["name"]
            list_of_artist_names.append(this_artists_name)
            this_artists_uri = result["artists"][0]["uri"]
            list_of_artist_uri.append(this_artists_uri)
            list_of_songs = result["name"]
            list_of_song_names.append(list_of_songs)
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
             'song': list_of_song_names,
             'song_uri': list_of_song_uri,
             'duration_ms': list_of_durations_ms,
             'explicit': list_of_explicit,
             'album': list_of_albums,
             'popularity': list_of_popularity
             })
        all_songs_saved = all_songs.to_csv('top50_songs.csv')

#Hier werden die Daten aus der Json-Datei in eine Text-Datei umgespeichert.
    filename = 'top50_data.json'
    with open(filename, 'r') as fr:
        pre_ = fr.read()
        lines = pre_.split('\n')
        new_filename = 'Json.txt'
        with open(new_filename, 'a') as fw:
            fw.write('\n'.join(lines))
    jsonfile = 'top50_data.json'

#Hier werden die Daten aus den Listen in ein Bild umgewandelt beziehungsweise als Grafik geordnet und angezeigt
    descending_order = all_songs['artist'].value_counts().sort_values(ascending=False).index
    ax = sb.countplot(y=all_songs['artist'], order=descending_order)

    sb.despine(fig=None, ax=None, top=True, right=True, left=False, trim=False)
    sb.set(rc={'figure.figsize': (6, 7.2)})

    ax.set_ylabel('')
    ax.set_xlabel('')
    ax.set_title('Songs per Artist in Top 50', fontsize=16, fontweight='heavy')
    sb.set(font_scale=1.4)
    ax.axes.get_xaxis().set_visible(False)
    ax.set_frame_on(False)

    y = all_songs['artist'].value_counts()
    for i, v in enumerate(y):
        ax.text(v + 0.2, i + .16, str(v), color='black', fontweight='light', fontsize=14)

    plt.savefig('top50_songs_per_artist.jpg', bbox_inches="tight")


# Mit Angaben zum Bild und dem bestehender PDF-Datei, wird das Bild zu einer PDF-Datei umgewandelt
    img_path = r"C:\Users\kevin\PycharmProjects\SpotifyAPI\top50_songs_per_artist.jpg"
    pdf_path = r"C:\Users\kevin\PycharmProjects\SpotifyAPI\Image.pdf"
    image = Image.open(img_path)
    pdf_bytes = img2pdf.convert(image.filename)
    file = open(pdf_path, "wb")
    file.write(pdf_bytes)
    image.close()
    file.close()
    print("Erfolgreich PDF-Datei erstellt")

# Für das E-Mail senden werden zuerst die Angaben gegeben. Account Daten zum Verschicken und die E-Mail Adresse
    # An die das Bild geschickt wird
    sender = "kayala766@gmail.com"
    password = "Info2matiker5"
    receiver = "kevinayala@gmx.ch"
    body = 'Endlich hat es funktioniert!'
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = 'This email has an attachment, a pdf file'

    message.attach(MIMEText(body, 'plain'))

    pdfname = 'Image.pdf'
    binary_pdf = open(pdfname, 'rb')

    payload = MIMEBase('application', 'octate-stream', Name=pdfname)
    # payload = MIMEBase('application', 'pdf', Name=pdfname)
    payload.set_payload((binary_pdf).read())

    # enconding the binary into base64
    encoders.encode_base64(payload)

    # add header with pdf name
    payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
    message.attach(payload)

    # use gmail with port
    session = smtplib.SMTP('smtp.gmail.com', 587)

    # enable security
    session.starttls()

    # login with mail_id and password
    session.login(sender, password)

    text = message.as_string()
    session.sendmail(sender, receiver, text)
    session.quit()
    print('Mail Sent');
    break;



