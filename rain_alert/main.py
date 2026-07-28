"""Docstring Here"""

import os

import requests

LAT = 34.637908
LON = -82.244851
API_KEY = os.environ.get("Open_Weather_API")
COUNT = 4

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "cnt": COUNT,
}

URL = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(URL, params=parameters, timeout=5)
response.raise_for_status()
weather_data = response.json()

city = weather_data.get("city", {}).get("name", "your area")

# need_umbrella = False
# for data in weather_data["list"]:
#     code = data['weather'][0]['id']
#     if code < 700:
#         need_umbrella = True

need_umbrella = any(item["weather"][0]["id"] < 700 for item in weather_data.get("list", []))

if need_umbrella:
    print(f"Chance of rain in {city}. Bring the umbrella.")
else:
    print(f"Sunny skies in {city} today. Enjoy the day.")


