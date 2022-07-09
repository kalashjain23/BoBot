import requests
import os
from dotenv import load_dotenv
load_dotenv()


def weather(city):
    API_ID = os.getenv("API_ID")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_ID}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        return weather

    else:
        return "ERROR!!"
