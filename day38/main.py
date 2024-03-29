import os
import requests
import datetime
from dotenv import load_dotenv

load_dotenv(r'C:\Users\nicol\Desktop\Development\100 days of code\day38\.env')

# url = "https://trackapi.nutritionix.com/v2"
# headers = {"x-app-id": os.environ.get('APP_ID'), "x-app-key": os.environ.get('APP_KEY')}
# body = {"query": "run 1 hour"}

# response = requests.post(url + '/natural/exercise', headers=headers, data=body)
# print(response.json())

###############
# response = requests.get(
#     'https://api.sheety.co/7da977ed9141fd0708a0ade259f48495/workout/feuille1')
# print(response.json())

###############
body = {"feuille1": {'date': datetime.datetime.now().strftime('%d/%m/%Y %Hh%M %Ss')}}
response = requests.post(
    'https://api.sheety.co/7da977ed9141fd0708a0ade259f48495/workout/feuille1',
    json=body,
    headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer " + os.environ.get('TOKEN')
    })
print(response.json())
