import os

import requests
import requests_cache
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

requests_cache.install_cache(expire_after=3600)

SHEETY_PRICES_ENDPOINT = (
    "https://api.sheety.co/7d6f5626ded2418525e0ecac2a0fa53c/flightDeals/prices"
)

load_dotenv()


class DataManager:

    def __init__(self):
        self._user = os.getenv("SHEETY_USERNAME")
        self._password = os.getenv("SHEETY_PASSWORD")
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_prices(self):
        response = requests.get(
            url=SHEETY_PRICES_ENDPOINT, auth=self._authorization, timeout=5
        )
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data
