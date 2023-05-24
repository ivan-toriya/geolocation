# %%
import requests
from dotenv import load_dotenv
import os
from get_wifi import get_wifi_data
import json

load_dotenv()
API_KEY = os.getenv("GEOLOCATION_API_KEY")  # TODO: Add your API key


BASE_URL = "https://www.googleapis.com/geolocation/v1/geolocate"
params = {"key": API_KEY}
wifi_list = get_wifi_data()
data = {"considerIp": "false", "wifiAccessPoints": wifi_list}

response = requests.post(BASE_URL, params=params, json=data)

if response.status_code == 200:
    lat, lng = response.json()["location"]["lat"], response.json()["location"]["lng"]
    print("-------- Google Maps Link --------")
    print(f"https://www.google.com/maps/?q={lat},{lng}")
print("-------- Response --------")
print(json.dumps(response.json(), indent=4))
print("-------- Requested MAC Addresses --------")
print(f"Number of MAC Addresses: {len(wifi_list)}")
print(f"Strongest signal strength: {max([x['signalStrength'] for x in wifi_list])}")
print(f"Weakest signal strength: {min([x['signalStrength'] for x in wifi_list])}")
print(
    f"Average signal strength: {sum([x['signalStrength'] for x in wifi_list]) / len(wifi_list)}"
)
print(json.dumps({"wifiAccessPoints": wifi_list}, indent=4))
