import requests
from twilio.rest import Client

# stock details
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# stock api data
stock_api_key = "OY31ZMP64QA7QY49"
stock_api_endpoint = "https://www.alphavantage.co/query"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key
}

# news api data
news_api_key = "bf4b4bb9828840268c53b0f108e51029"
news_api_endpoint = "https://newsapi.org/v2/everything?"
news_parameters = {
    'apiKey':news_api_key,
    'q': STOCK,
    'language': 'en'
}

# twilio api data
account_sid = "AC6df112f0b91b08da20efb1b7d93569ed"
auth_token = "da8d96a52ac69628e3d70418fe9ed4fe"
my_twilio_number = +13134762190

# getting last 2 days price of stock and the percentage difference between yesterday and day before yesterday's stock price.
response = requests.get(url=stock_api_endpoint,params=stock_parameters,verify=False)
response.raise_for_status()

data = response.json()['Time Series (Daily)']

data_list = [value for (key,value) in data.items()]
# print(data_list)

yesterday_closing_price = float(data_list[0]['4. close'])
day_before_yesterday_closing_price = float(data_list[1]['4. close'])

percentage_diff = abs(((yesterday_closing_price - day_before_yesterday_closing_price) / yesterday_closing_price) * 100)

print(percentage_diff)

# if the percentage difference between stock price is more than 0.10, get news of the stock.
if percentage_diff > 0.10:
    news_response = requests.get(url=news_api_endpoint,params=news_parameters,verify=False)
    news_response.raise_for_status()
    news_data = news_response.json()['articles']
    articles = news_data[:3]
    articles_to_send = [f"{STOCK}\nHeadlines:{article['title']}\n Brief:{article['description']}" for article in articles]
    # sending the stock news as a message
    for article in articles_to_send:
        client = Client(account_sid,auth_token)
        message = client.messages.create(
            from_=my_twilio_number,
            body=article,
            to='+916382727512'
        )
        # getting the message status and sid for future reference.
        print(f"message status is {message.status}")
        print(f"message sid is {message.sid}")


