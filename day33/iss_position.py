import requests
from datetime import datetime
import time
from math import sqrt
import config.config as config

MY_LAT = 45.194260
MY_LONG = 5.731670

settings = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0,
    }

def get_iss_position():
    iss_response = requests.get('http://api.open-notify.org/iss-now.json')

    iss_data = iss_response.json()

    iss_longitude = float(iss_data['iss_position']['longitude'])
    iss_latitude = float(iss_data['iss_position']['latitude'])

    return iss_longitude, iss_latitude

#------------------------------------------
def get_current_sunrise_sunset():
    now = datetime.now()

    sunrise_sunset_response = requests.get('https://api.sunrise-sunset.org/json', params=settings)
    sunrise_sunset_data = sunrise_sunset_response.json()

    sunrise = datetime.strptime(sunrise_sunset_data['results']['sunrise'].replace('T', ' ').split('+')[0], "%Y-%m-%d %H:%M:%S")
    sunset = datetime.strptime(sunrise_sunset_data['results']['sunset'].replace('T', ' ').split('+')[0], "%Y-%m-%d %H:%M:%S")

    return now, sunset, sunrise

def check_if_in_country(lat, long):
    url = 'https://maps.googleapis.com/maps/api/geocode/json'

    params = {
        'latlng': f'{lat},{long}',
        'key': config.google_api_key,
    }

    response = requests.get(url, params=params)
    batch = []
    try:
        for data in response.json()['results'][1]['address_components']:
            batch.append(data['long_name'])
        return batch
    except IndexError:
        return 'lost in the sea'

while True:
    iss_longitude, iss_latitude = get_iss_position()

    now, sunset, sunrise = get_current_sunrise_sunset()

    distance = sqrt((iss_latitude - MY_LAT) ** 2 + (iss_longitude - MY_LONG) ** 2)

    if now < sunrise or now > sunset:
        if (MY_LAT - 5 < iss_latitude < MY_LAT + 5) and (MY_LONG - 5 < iss_longitude < MY_LONG + 5):
            print('The ISS is close to me and it\'s dark, I can see it')
        else:
            # print(f'LAT diff = {round(abs(iss_latitude - MY_LAT), 2)}, LONG diff = {round(abs(iss_longitude - MY_LONG), 2)}')
            print(iss_longitude, iss_latitude)

    print(check_if_in_country(iss_latitude, iss_longitude))
    time.sleep(2)
