from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


date = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ")

url = 'https://www.billboard.com/charts/hot-100/' + date

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url=url,headers=header)

webpage = response.text
# print(webpage)

soup = BeautifulSoup(webpage,'html.parser')
song_name_spans = soup.select("li ul li h3")

song_names = [song.getText().strip() for song in song_name_spans]
print(song_names)

client_id = '68aa928190954e00840039ea1cd862d5'
client_secret = '7747994565b8400c85a9eda1bb47166d'
redirect_url = 'https://open.spotify.com/'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",client_id= client_id,client_secret=client_secret,redirect_uri=redirect_url,cache_path="token.txt",show_dialog=True,username="pythontestingmail"))

user_id = sp.current_user()["id"]
print(user_id)




