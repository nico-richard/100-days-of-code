from calendar import day_abbr
import requests
import sys
sys.path.insert(1, r'C:\Users\nicol\Desktop\100 days of code')
# sys.path.insert(1, r'C:\Users\33638\OneDrive\Bureau\PYTHON\100-days-of-code')
import config.config as config
import datetime as dt

COMPANY_NAME = "Tesla Inc"
STOCK_NAME = "TSLA"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_stock_difference(STOCK_NAME):

    NOW = dt.datetime.now()

    stock_url = 'https://www.alphavantage.co/query'
    stock_params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOCK_NAME,
        'interval': '60min',
        'apikey': config.alphavantage_api_key,
    }
    stock_response = requests.get(url=stock_url, params=stock_params)
    stock_response.raise_for_status()
    stock_data = stock_response.json()

    days_before = 1 if (NOW.hour > 16) else 1

    d_1 = NOW.date() - dt.timedelta(days=days_before)

    if d_1.weekday() == 0: #monday
        d_2 = d_1 - dt.timedelta(days=3) #friday
    else:
        d_2 = d_1 - dt.timedelta(days=1)
    
    d_1_data = stock_data['Time Series (Daily)'][f'{d_1}']
    d_2_data = stock_data['Time Series (Daily)'][f'{d_2}']

    return round((float(d_1_data['1. open']) - float(d_2_data['1. open'])) / float(d_1_data['1. open']) * 100, 2), d_1, d_2

stock_diff, d_1, d_2 = get_stock_difference(STOCK_NAME)

print(f'----- {stock_diff} % between {d_2} and {d_1} -----\n')

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_news_from(COMPANY_NAME):

    news_url = 'https://newsapi.org/v2/top-headlines'
    news_params = {
        'q': COMPANY_NAME,
        'apiKey': config.news_api_key,
    }
    news_response = requests.get(url=news_url, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    return news_data

if abs(stock_diff) >= 5:
    print('The absolute stock diff was > 5%\n')
    news_data = get_news_from(COMPANY_NAME)

    print(f'Article(s) found : {news_data["totalResults"]}')

    if news_data["totalResults"]:
        for article in news_data['articles']:
            for key, value in article.items():
                print(f'{key} \t: {value}')
else:
    print('The absolute stock diff was < 5%\n')

print('----------------------------------------------------')

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

