import requests
import json

ip = input("Enter IP: ")
response = requests.get(f"https://geolocation-db.com/json/{ip}&position=true").json()
print(json.dumps(response, indent=4, sort_keys=False, default=str))