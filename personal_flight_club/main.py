# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
from pprint import pprint

import requests
from data_manager import DataManager
from dotenv import load_dotenv
from flight_data import FlightData
from flight_search import FlightSearch

dt_tomorrow = datetime.now() + timedelta(days=1)
dt_six_months = datetime.now() + timedelta(days=2)

tomorrow = dt_tomorrow.strftime("%Y-%m-%d")
six_months = dt_six_months.strftime("%Y-%m-%d")

get_data = DataManager()
sheet_data = get_data.get_prices()


origin_city_code = "LHR"
destination_city_code = "CDG"
from_time = tomorrow
to_time = six_months

get_flights = FlightSearch()
search_data = get_flights.check_flights(
    origin_city_code, destination_city_code, from_time, to_time
)

data_parser = FlightData()
parsed_data = data_parser.price_checker(search_data)
