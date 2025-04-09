import requests
import datetime

USERNAME = "sunapana"
TOKEN = "alertarumugam"
HEADER = {"X-USER-TOKEN" : TOKEN}

pixela_endpoint = "https://pixe.la/v1/users"

pixela_parameters = {
    "token": TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# response = requests.post(url=pixela_endpoint,json=pixela_parameters)
# print(response.text)

graphs_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
"https://pixe.la/v1/users/sunapana/graphs"
graphs_parameters = {
    "id" : "sunapana007",
    "name" : "Study Tracker",
    "unit" : "minutes",
    "type" : "int",
    "color" : "shibafu"
}

today = datetime.datetime.now()



# graph_response = requests.post(url=graphs_endpoint,json=graphs_parameters,headers={"X-USER-TOKEN" : TOKEN})
#
# print(graph_response.text)

data = {
    "date": today.strftime("%Y%m%d"),
    "quantity" : input("How Many Minutes did you study today? ")
}

graphs_data_endpoint = f"{graphs_endpoint}/{graphs_parameters['id']}"
graphs_data = requests.post(url=graphs_data_endpoint,headers=HEADER,json=data)
print(graphs_data.text)

update_data = f"{graphs_data_endpoint}/20240611"

new_data = {
    "quantity" : "140"
}

# response = requests.put(url=update_data,headers=HEADER,json=new_data)
#
# response = requests.delete(url=update_data,headers=HEADER)
# print(response.text)