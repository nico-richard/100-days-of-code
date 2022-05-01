import config.config as config
import requests, json, sys

url = config.slack_url
# message = ("A Sample Message")
# title = (f"New Incoming Message :zap:")

slack_data = {
    "channel" : "C03E1Q31AHE",
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Vous voulez voir quelque chose de beau ?"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Oui"
					},
					"style": "primary",
					"url": "https://bonjourmadame.fr"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Non"
					},
					"style": "danger",
					"url": "https://www.bonjourponey.fr/"
				}
			]
		}
	]
}
byte_length = str(sys.getsizeof(slack_data))
headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
response = requests.post(url, data=json.dumps(slack_data), headers=headers)
if response.status_code != 200:
    raise Exception(response.status_code, response.text)