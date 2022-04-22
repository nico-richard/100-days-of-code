import requests
import config.config as config

# Current location  ----------------------------------------------------
url = 'http://api.openweathermap.org/geo/1.0/reverse'
parameters = {
    'lat': '47.01',
    'lon': '4.83',
    'appid': config.weather_api_key,
}
# --------------------------------------------------------------------

response = requests.get(url=url, params=parameters)
response.raise_for_status()
data = response.json()

# for language, name in data[0]['local_names'].items():
#     print(language, name)
print(data[0]['name'])