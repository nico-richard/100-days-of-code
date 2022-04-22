import requests
import datetime as dt
import config.config as config

# # Current weather ----------------------------------------------------
# url = 'https://api.openweathermap.org/data/2.5/weather'
# parameters = {
#     'q': 'grenoble',
#     'appid': config.weather_api_key,
# }
# # --------------------------------------------------------------------

# Forecast -----------------------------------------------------------
url = 'https://api.openweathermap.org/data/2.5/onecall'
parameters = {
    'lat': 45.194260,
    'lon': 5.731670,
    'appid': config.weather_api_key,
    'exclude': 'current, minutely, daily, alerts'
}
# --------------------------------------------------------------------

response = requests.get(url=url, params=parameters)
response.raise_for_status()
data = response.json()

# Forecast -----------------------------------------------------------
for hour in data['hourly']:
    weather = hour['weather'][0]['description']
    # temp = round(hour['temp'] - 273, 2)
    ts = int(hour['dt'])
    # clouds = hour['clouds']
    datetime = dt.datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H') + 'h'
    # print(datetime + ' : ' + str(temp) + '°C ' + str(clouds) + '%')
    print(f'{datetime} : {weather}')
# --------------------------------------------------------------------
# print(data)
# # Current weather ----------------------------------------------------
# print(data)
# # --------------------------------------------------------------------