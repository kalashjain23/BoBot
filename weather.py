import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_id = os.getenv("API_ID")


def weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        description = data['weather'][0]['description']
        return description

    else:
        return "ERROR!!"


def temp(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        return round(temperature - 273.15, 3)

    else:
        return "ERROR!!"
