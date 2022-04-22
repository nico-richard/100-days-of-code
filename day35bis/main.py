import requests
import datetime as dt
from twilio.rest import Client

account_sid = 'ACc26a38a2609649a63cbd67130f12be4c'
auth_token = 'ff10a998a8c1cb3b0cdcc2bbb68e49af'

client = Client(account_sid, auth_token)

url = 'https://api.openweathermap.org/data/2.5/onecall'
params = {
    'lat': 45.194260,
    'lon': 5.731670,
    'appid': 'a0fb0b7788f77a45fa4dda8b20f5643a',
    'exclude': 'current,minutely,daily,alerts'
}

response = requests.get(url=url, params=params)
response.raise_for_status()
data = response.json()

now = dt.datetime.now()

twelve_hours_data = data['hourly']
hourly_weather = []

hourly_weather = [{'time': time, 'weather': hourly_data['weather']}
                for hourly_data in twelve_hours_data
                if 7 <= (time := dt.datetime.fromtimestamp(hourly_data["dt"])).hour <= 19 and time.day == now.day + 1]

weather_ids = [[weather['id'] for weather in item['weather']] for item in hourly_weather]
weather_descriptions = [[weather['description'] for weather in item['weather']] for item in hourly_weather]
rainy_hours = ['Rainy' if (id_ <= 700) else 'Not rainy' for ids in weather_ids for id_ in ids]

body = 'Take umbrella, it is going to rain today ☔ \n' if any(id_ <= 700 for ids in weather_ids for id_ in ids) else 'It will not rain today 🌤️'
h = 7
for hour in rainy_hours:
    body += f'{h}h : {hour} \n'
    h += 1


message = client.messages \
                .create(
                     body=body,
                     from_='+14152376013',
                     to='+33638396077'
                 )
# print(rainy_hours)