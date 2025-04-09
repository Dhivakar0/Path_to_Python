import requests

paramters ={'amount': 10,
            'category':18,
            'type':'boolean'
            }

response = requests.get(url="https://opentdb.com/api.php?",params=paramters,verify=False)

response.raise_for_status()

question_data = response.json()['results']

