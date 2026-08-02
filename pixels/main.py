"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp
*** Pixela API Integration ***
This program demonstrates how to interact with the Pixela API to track personal metrics. It covers user creation,
graph creation, and pixel posting. The code includes examples of HTTP POST requests and date formatting.

Python Concepts Highlighted:
- `requests` library for making HTTP requests (`requests.post()`)
- `datetime` module for working with dates (`datetime.now()`, `strftime()`)
- F-strings for dynamic string formatting (`f"..."`)
- Dictionary for structuring API request parameters (`parameters`, `graph_parameters`, `payload`)
- Global constants for configuration (`USERNAME`, `TOKEN`, `GRAPH_ID`)
"""

from datetime import datetime

import requests

# Global Constants:
# `USERNAME`: Stores the Pixela username for API authentication and URL construction.
USERNAME = "big-matt"
# `TOKEN`: Stores the Pixela API token for authentication. This token acts as an API key.
TOKEN = "Pcks3lA-pword"
# `GRAPH_ID`: Unique identifier for the graph to which pixels will be posted. Used in API endpoint URLs.
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

# `parameters`: Dictionary containing parameters for creating a new Pixela user.
# `token`: The user's Pixela token.
# `username`: The desired username for the Pixela account.
# `agreeTermsOfService`: Must be "yes" to agree to the Pixela terms of service.
# `notMinor`: Must be "yes" to confirm the user is not a minor.
parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# *** User Creation (Commented Out) ***
# Uncomment the following lines to create a new Pixela user.
# `requests.post()`: Sends an HTTP POST request to the Pixela user creation endpoint.
# `url`: The `pixela_endpoint`.
# `json`: The `parameters` dictionary, sent as a JSON payload.
# response = requests.post(url=pixela_endpoint, json=parameters)
# `response.text`: Prints the response from the Pixela API, indicating success or failure.
# print(response.text)

# `graph_endpoint`: Constructs the API endpoint for creating a new graph for the specified user.
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# `headers`: Dictionary containing the request headers, including the user token for authentication.
# `X-USER-TOKEN`: The Pixela user token, required for authenticating graph creation requests.
headers = {
    "X-USER-TOKEN": TOKEN,
    }

# `graph_parameters`: Dictionary containing the parameters for creating a new graph.
# `id`: A unique ID for the new graph.
# `name`: The display name of the graph (e.g., "Weight").
# `unit`: The unit of measurement for the graph (e.g., "lbs").
# `type`: The data type of the graph values (e.g., "float", "int").
# `color`: The color of the graph (e.g., "sora", "ajisai", "kuro").
# `timezone`: The timezone for the graph, important for accurate date tracking.
graph_parameters = {
    "id":"graph1",
    "name":"Weight",
    "unit":"lbs",
    "type":"float",
    "color":"sora",
    "timezone":"America/New_York"
}

# *** Graph Creation (Commented Out) ***
# Uncomment the following lines to create a new graph.
# `requests.post()`: Sends an HTTP POST request to the graph creation endpoint.
# `url`: The `graph_endpoint`.
# `json`: The `graph_parameters` dictionary, sent as a JSON payload.
# `headers`: The `headers` dictionary containing the authentication token.
# `timeout`: Sets a timeout for the request to prevent indefinite waiting.
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers, timeout=5)
# `response.text`: Prints the response from the Pixela API, indicating success or failure.
# print(response.text)

# `dt`: Stores the current date and time using `datetime.now()`.
dt = datetime.now()

# `update_endpoint`: Constructs the API endpoint for posting a new pixel (updating the graph).
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# `payload`: Dictionary containing the data for the new pixel.
# `date`: The date for the pixel, formatted as "YYYYMMDD" using `strftime()`.
# `quantity`: The value to be recorded for the pixel (e.g., "247.1" for weight).
payload = {
    "date": dt.strftime("%Y%m%d"),
    "quantity": "247.1",
}

# *** Pixel Posting ***
# `requests.post()`: Sends an HTTP POST request to the pixel posting endpoint.
# `url`: The `update_endpoint`.
# `json`: The `payload` dictionary, sent as a JSON payload.
# `headers`: The `headers` dictionary containing the authentication token.
# `timeout`: Sets a timeout for the request.
response = requests.post(url=update_endpoint, json=payload, headers=headers, timeout=5)
# `response.text`: Prints the response from the Pixela API after attempting to post a pixel.
print(response.text)
