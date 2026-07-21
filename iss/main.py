
"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** ISS Overhead Notifier ***
This program checks if the International Space Station (ISS) is currently overhead
a specified location and if it's dark enough to see it. It then notifies the user.

Python Concepts Highlighted:
- `datetime` module for working with dates and times (`datetime.now`)
- `time` module for pausing program execution (`time.sleep`)
- `requests` library for making HTTP GET requests to external APIs (`requests.get`, `response.json`)
- Global constants for user-defined coordinates (`MY_LAT`, `MY_LONG`)
- Conditional logic for checking ISS proximity and night time (`if/else` statements)
- Function modularity for breaking down complex tasks (`where_is_iss_now`, `night_time`)
- API interaction with `api.open-notify.org` for ISS position and 
  `api.sunrise-sunset.org` for daylight hours.
"""

from datetime import datetime
import time
import requests

# --- GLOBAL CONSTANTS ---
# Your geographical latitude. Used to determine if the ISS is overhead.
# These values should be updated to your specific location.
MY_LAT = 34.694397  # Example: Latitude for Greenville, SC, USA
# Your geographical longitude. Used to determine if the ISS is overhead.
MY_LONG = -82.200594 # Example: Longitude for Greenville, SC, USA


def where_is_iss_now():
    """Checks if the International Space Station (ISS) is currently within a 5-degree radius
    of the predefined `MY_LAT` and `MY_LONG` coordinates.

    This function makes an API call to `http://api.open-notify.org/iss-now.json` to get the
    current latitude and longitude of the ISS. It then compares these coordinates with the
    user\'s location.

    Args:
        None

    Returns:
        bool: `True` if the ISS is within 5 degrees of the user\'s location, `False` otherwise.
    """

    response = requests.get(url="http://api.open-notify.org/iss-now.json", timeout=5)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT - 5 < iss_latitude < MY_LAT + 5) and (MY_LONG - 5 < iss_longitude < MY_LONG + 5):
        return True
    return False


def night_time():
    """Determines if it is currently nighttime at the predefined `MY_LAT` and `MY_LONG` coordinates.

    This function makes an API call to `https://api.sunrise-sunset.org/json` to get the sunrise
    and sunset times for the user\'s location. It then compares the current hour with these times
    to ascertain if it\'s dark.

    Args:
        None

    Returns:
        bool: `True` if the current time is after sunset or before sunrise (i.e., nighttime),
              `False` otherwise.
    """
    # Parameters for the sunrise-sunset API request.
    parameters = {
        "lat": MY_LAT,  # User\'s latitude.
        "lng": MY_LONG, # User\'s longitude.
        "formatted": 0, # Request raw (unformatted) time data.
    }

    # Make a GET request to the sunrise-sunset API with the specified parameters.
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, timeout=5)
    # Raise an HTTPError for bad responses (4xx or 5xx status codes).
    response.raise_for_status()
    # Parse the JSON response.
    data = response.json()

    # Extract sunrise and sunset hours from the response.
    # The time is in ISO 8601 format, so we split to get the hour.
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Get the current hour in 24-hour format.
    time_now = datetime.now()

    # Check if the current hour falls outside the daylight hours (after sunset or before sunrise).
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True  # It is nighttime.
    return False     # It is daytime.


# --- MAIN PROGRAM LOOP ---
# This loop continuously checks for the ISS position and visibility, pausing between checks.
while True:
    # Check if the ISS is overhead AND it is currently nighttime at the user\'s location.
    if where_is_iss_now() and night_time():
        print("The ISS is overhead and it is visible!") # Notify user if both conditions are met.
    else:
        print("The ISS is currently not visible.")     # Notify user if the ISS is not visible.

    # Pause the program for 120 seconds (2 minutes) before checking again.
    # This prevents excessive API calls and reduces resource usage.
    time.sleep(120)
