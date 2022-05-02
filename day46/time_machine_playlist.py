from bs4 import BeautifulSoup
import requests
import sys
sys.path.insert(1, r'C:\Users\nicol\Desktop\100 days of code')
import config.config as config
import spotipy
from spotipy.oauth2 import SpotifyOAuth

spotify_oauth = SpotifyOAuth(client_id=config.spotify_client_id, client_secret=config.spotify_client_secret,
    redirect_uri='http://example.com', show_dialog=True, scope="playlist-modify-private")

sp = spotipy.Spotify(auth_manager=spotify_oauth)

user_id = sp.current_user()["id"]
results = sp.search(q='artist:queen', type='track', limit=2)
print(results['tracks'])

date = '2000-08-05'

response = requests.get('https://www.billboard.com/charts/hot-100/' + date)
html_data = response.text

soup = BeautifulSoup(html_data, 'html.parser')

titles = soup.select(selector='li ul li h3.c-title#title-of-a-story')
artists = soup.select(selector="li ul li span.c-label.a-no-trucate")

# for title, artist in zip(titles, artists):
#     print(title.text.strip(), artist.text.strip())

