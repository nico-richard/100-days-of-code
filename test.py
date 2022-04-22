import json
import requests
import config.config as config

if __name__ == '__main__':
    url = config.slack_url
    message = ("A Sample Message")
    title = (f"New Incoming Message :zap:")
    slack_data = {
        "username": "BigBot",
        "icon_emoji": ":star:",
        # "channel" : "#somerandomcahnnel",
        "attachments": [
            {
                "color": "#9733EE",
                "fields": [
                    {
                        "title": title,
                        "value": message,
                        "short": "false",
                    }
                ]
            }
        ]
    }
    response = requests.post(url, data=json.dumps(slack_data))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)