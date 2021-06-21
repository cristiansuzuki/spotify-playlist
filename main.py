import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

scope = 'playlist-modify-public'
username = 'cristiansuzuki'

token = SpotifyOAuth(scope=scope, username=username)

spotifyObject = spotipy.Spotify(auth_manager = token)

# Criar playlist

playlist_name = input("Insira o nome da playlist: ")
playlist_description = input("Insira a descrição da playlist: ")

spotifyObject.user_playlist_create(user=username, name=playlist_name, public=True, description=playlist_description)

user_input = input("Insira o nome da música: ")

musicas = []

while user_input != "fim":
    resultado = spotifyObject.search(q=user_input)
    musicas.append(resultado['tracks']['items'][0]['uri'])
    user_input = input("Insira o nome da música: ")
    
prePlaylist = spotifyObject.user_playlists(user=username)

playlist = prePlaylist['items'][0]['id']

#Adicionar músicas na playlist
spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=musicas)
    