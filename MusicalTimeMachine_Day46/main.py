from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#Client details for Spotipy API
CLIENT_ID = ''
CLIENT_SECRET = ''
USERNAME = ''
song_list = []

#Creating spotipy object
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.org/callback",
        client_id= CLIENT_ID,
        client_secret= CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username= USERNAME, 
    )
)
user_id = sp.current_user()["id"]

#Getting the day for which user wants to create the musical time machine for
#Getting the billboard hot 100 chart for that day
day = input("Which year do you want to travel to? Type the date in YYYY-MM-DD format.")
URL = f"https://www.billboard.com/charts/hot-100/{day}"
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36",
}
response = requests.get(url=URL,headers=headers)
data = response.text

#Scrapping the data from the billboard hot 100 data received
Soup = BeautifulSoup(data,"html.parser")
header_tag = Soup.findAll(name = "h3", class_ = "u-max-width-230@tablet-only")
for header in header_tag:
    song = header.get_text()
    song_name = song.replace("\t","").replace("\n","")
    song_list.append(song_name)

#Getting the song year and searching for the songs on spotify
#Creating a list of song URIs    
song_year = day.split("-")[0]
song_uris = []
for song in song_list:
    result = sp.search(q=f"track:{song} year:{song_year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating the playlist for the year and add all the songs available on Spotify
result = sp.user_playlist_create(user=user_id,name=f'Musical Time Machine {song_year}',public=False)
playlist_id = result['id']
response = sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)

