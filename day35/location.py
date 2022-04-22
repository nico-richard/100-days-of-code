import requests

# Current location  ----------------------------------------------------
url = 'http://api.openweathermap.org/geo/1.0/reverse'
parameters = {
    'lat': '47.01',
    'lon': '4.83',
    'appid': 'a0fb0b7788f77a45fa4dda8b20f5643a'
}
# --------------------------------------------------------------------

response = requests.get(url=url, params=parameters)
response.raise_for_status()
data = response.json()

# for language, name in data[0]['local_names'].items():
#     print(language, name)
print(data[0]['name'])