import requests

target_url = "http://api.open-notify.org/iss-now.json"

response = requests.get(target_url)
response.raise_for_status()

data = response.json()
longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

print(latitude, longitude)