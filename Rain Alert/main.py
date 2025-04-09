import requests
from twilio.rest import Client

kadugodi_lat = 13.005010
kadugodi_lon = 77.729233

API_KEY = "308c015dc1a78b7314acedd83219dfc4"
api_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

account_sid = "AC6df112f0b91b08da20efb1b7d93569ed"
auth_token = "da8d96a52ac69628e3d70418fe9ed4fe"

my_twilio_number = +13134762190

parameters = {
    "lat": kadugodi_lat,
    "lon": kadugodi_lon,
    "appid": API_KEY,
    "cnt":4
}

response = requests.get(url=api_endpoint, params=parameters)
response.raise_for_status()

weather_data = response.json()

will_rain = False

for hourly_data in weather_data['list']:
    condition_code = hourly_data['weather'][0]['id']
    if condition_code < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid,auth_token)
#     message = client.messages.create(
#         from_=my_twilio_number,
#         body="It's going to rain today.Take an Umbrella!",
#         to='+916382727512'
#     )
#     print(f"message status is {message.status}")
#     print(f"message sid is {message.sid}")
#
#     message = client.messages("SM7e481ce0ae936a53c1945a08f4bf16a6").fetch()
#     print(message.status)

else:
    client = Client(account_sid,auth_token)
    message = client.messages("SMf50d5d23e1963c030b303a970db94eac").fetch()
    print(message.status)




