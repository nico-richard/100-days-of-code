from bs4 import BeautifulSoup
import requests
import webbrowser
import sys
sys.path.insert(1, r'C:\Users\nicol\Desktop\100 days of code')
import config.config as config
import json

response = requests.get('https://www.meteoblue.com/fr/meteo/prevision/meteograms/grenoble_france_3014728')
html_data = response.text

soup = BeautifulSoup(html_data, 'html.parser')

meteogram_url = 'http:' + soup.find(class_='image-lazyload').get('data-original')

data = requests.get(meteogram_url)

# webbrowser.open('http://' + meteogram)
# with open('meteogram.png', 'wb') as file:
#     file.write(data.content)

slack_url = config.slack_url
channel = '#D01E78XTALD'
headers = {'Content-type': 'application/json'}
message = {
    # "channel": channel,
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Meteo for the next 5 days :"
			}
		},
		{
			"type": "image",
			"title": {
				"type": "plain_text",
				"text": "meteogram"
			},
			"image_url": meteogram_url,
			"alt_text": "meteogram image"
		}
	]
}

response = requests.post(slack_url, headers=headers, data=json.dumps(message))
response.raise_for_status()