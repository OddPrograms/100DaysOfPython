import requests
import os
from dotenv import load_dotenv # pip install python-dotenv

load_dotenv("./EnvironmentVariables/.env")
latitude = os.getenv("lat") # in .env lat=""
longitude = os.getenv("lon") # in .env lon=""

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": "261ce2fb1d2372b189adddb3523bb943",
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=parameters)
print(response.status_code)
weather_data = response.json()

weather_codes = []

for i in range(1,12):
    weather_codes.append(weather_data["list"][i]["weather"][0]["id"])

will_rain = False

for i in weather_codes:
    if i < 700:
        print("Bring an Umbrella.")
        break
    else:
        pass
