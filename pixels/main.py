"""Docstring Here"""

from datetime import datetime

import requests

USERNAME = "big-matt"
TOKEN = "Pcks3lA-pword"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN,
    }

graph_parameters = {
    "id":"graph1",
    "name":"Weight",
    "unit":"lbs",
    "type":"float",
    "color":"sora",
    "timezone":"America/New_York"
}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers, timeout=5)
# print(response.text)

# date
# weight
dt = datetime.now()


update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# https://pixe.la/v1/users/big-matt/graphs
payload = {
    "date": dt.strftime("%Y%m%d"),
    "quantity": "247.1",
}
response = requests.post(url=update_endpoint, json=payload, headers=headers, timeout=5)
print(response.text)