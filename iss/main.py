import requests
from datetime import datetime
import time

MY_LAT = 34.694397 # Your latitude
MY_LONG = -82.200594 # Your longitude

def where_is_iss_now():
        
    iss_overhead = False
    dark = False
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT - 5 < iss_latitude < MY_LAT + 5) and (MY_LONG - 5 < iss_longitude < MY_LONG + 5):
        iss_overhead = True

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    # Check if current hour is after sunset OR before sunrise
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        dark = True

    if iss_overhead and dark:
        print("The ISS is overhead and it is visible")
    else:
        print("The ISS is currently not visible")
    # and it is currently dark
    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.
    print(iss_latitude)
    print(iss_longitude)
    time.sleep(5)
    where_is_iss_now()

where_is_iss_now()
# Main Loop
while True:
    if iss_overhead() and is_night():
        print("The ISS is overhead and it is visible!")
    else:
        print("The ISS is currently not visible.")

    time.sleep(5)


