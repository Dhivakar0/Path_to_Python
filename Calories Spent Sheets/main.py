import requests

nutrionix_api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutrionix_api_id = "828d8f59"
nutrionix_api_key = "5bbf960341f796b225325188794fb43a"

headers = {
    "x-app-id" : nutrionix_api_id,
    "x-app-key" : nutrionix_api_key,
    "Content-Type": "application/json"
}

# nutrionix_parameters = {
#     "Response Format" : "JSON" ,
#     "Requires Authentication" : "Yes",
#     "HTTP Method" : "POST",
#     "Host Domain": "https://trackapi.nutritionix.com",
#     "Endpoint":"/v2/natural/exercise"
#  }

data = {
    "query" : "Run for 4 km and swim for 2 kms"
}

response = requests.post(url=nutrionix_api_endpoint,json=data,headers=headers)

if response.status_code == 200:
    print(response.json()['exercises'['']])
else:
    print(f"Request failed with status code{response.status_code}")
    print(response.text)



