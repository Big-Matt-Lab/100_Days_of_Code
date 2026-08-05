import os

import requests
from dotenv import load_dotenv

SERP_ENDPOINT = "https://serpapi.com/search.json"
load_dotenv()


class FlightSearch:
    def __init__(self):
        self._api_key = os.getenv("SERP_API_KEY")

    def check_flights(
        self, origin_city_code, destination_city_code, from_time, to_time
    ):
        parameters = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time,
            "return_date": to_time,
            "type": "1",
            "adults": "1",
            "currency": "USD",
            "api_key": self._api_key,
        }
        response = requests.get(url=SERP_ENDPOINT, params=parameters, timeout=5)
        search_data = response.json()
        return search_data
