import requests
import random

lat = random.random() * 180 - 90
long = random.random() * 180 - 90

# lat = 48.73160688063447
# long = 73.95429423121004

url = 'https://maps.googleapis.com/maps/api/geocode/json'

params = {
    'latlng': f'{lat},{long}',
    'key': "AIzaSyCfCRtGsfCjToANLElqXtu_gH1y2fxKIlg",
}

print(lat)
print(long)
response = requests.get(url, params=params)
try:
    for data in response.json()['results'][1]['address_components']:
        print(data['long_name'])
except IndexError:
    print('lost in the sea')