# ... existing code ...
import time
from datetime import datetime

import requests

# --- GLOBAL CONSTANTS ---
# Your geographical latitude. Used to determine if the ISS is overhead.
# These values should be updated to your specific location.
MY_LAT = 34.694397  # Example: Latitude for Greenville, SC, USA
# Your geographical longitude. Used to determine if the ISS is overhead.
MY_LONG = -82.200594  # Example: Longitude for Greenville, SC, USA

# API Endpoints
ISS_API_URL = "http://api.open-notify.org/iss-now.json"
SUNRISE_SUNSET_API_URL = "https://api.sunrise-sunset.org/json"

# Configuration for ISS proximity and check interval
ISS_PROXIMITY_DEGREES = 5
CHECK_INTERVAL_SECONDS = 120


def where_is_iss_now(user_latitude: float, user_longitude: float) -> bool:
    """Checks if the International Space Station (ISS) is currently within a predefined radius
    of the given user coordinates.

    This function makes an API call to `http://api.open-notify.org/iss-now.json` to get the
    current latitude and longitude of the ISS. It then compares these coordinates with the
    user's location.

    Args:
        user_latitude (float): The latitude of the user's location.
        user_longitude (float): The longitude of the user's location.

    Returns:
        bool: `True` if the ISS is within `ISS_PROXIMITY_DEGREES` of the user's location, `False` otherwise.
    """
    response = requests.get(url=ISS_API_URL, timeout=5)
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +ISS_PROXIMITY_DEGREES or -ISS_PROXIMITY_DEGREES of the ISS position.
    return (
        user_latitude - ISS_PROXIMITY_DEGREES
        < iss_latitude
        < user_latitude + ISS_PROXIMITY_DEGREES
    ) and (
        user_longitude - ISS_PROXIMITY_DEGREES
        < iss_longitude
        < user_longitude + ISS_PROXIMITY_DEGREES
    )


def night_time(user_latitude: float, user_longitude: float) -> bool:
    """Determines if it is currently nighttime at the given user coordinates.
    This function makes an API call to `https://api.sunrise-sunset.org/json` to get the sunrise
    and sunset times for the user's location. It then compares the current hour with these times
    to ascertain if it's dark.
    Args:
        user_latitude (float): The latitude of the user's location.
        user_longitude (float): The longitude of the user's location.
    Returns:
        bool: `True` if the current time is after sunset or before sunrise (i.e., nighttime),
              `False` otherwise.
    """
    # Parameters for the sunrise-sunset API request.
    parameters = {
        "lat": user_latitude,  # User's latitude.
        "lng": user_longitude,  # User's longitude.
        "formatted": 0,  # Request raw (unformatted) time data.
    }
    # Make a GET request to the sunrise-sunset API with the specified parameters.
    response = requests.get(SUNRISE_SUNSET_API_URL, params=parameters, timeout=5)
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
    return time_now.hour >= sunset or time_now.hour <= sunrise


# --- MAIN PROGRAM LOOP ---
# This loop continuously checks for the ISS position and visibility, pausing between checks.
while True:
    # Check if the ISS is overhead AND it is currently nighttime at the user's location.
    if where_is_iss_now(MY_LAT, MY_LONG) and night_time(MY_LAT, MY_LONG):
        print(
            "The ISS is overhead and it is visible!"
        )  # Notify user if both conditions are met.
    else:
        print(
            "The ISS is currently not visible."
        )  # Notify user if the ISS is not visible.
    # Pause the program for CHECK_INTERVAL_SECONDS (2 minutes) before checking again.
    # This prevents excessive API calls and reduces resource usage.
    time.sleep(CHECK_INTERVAL_SECONDS)
