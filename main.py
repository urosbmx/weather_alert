from model import WeatherData
from weather import Weather
import json
from dotenv import load_dotenv
import os
import requests
import notification
import message

load_dotenv()

api_key = os.getenv('API_KEY')
url = os.getenv('URL')
my_email = os.getenv("EMAIL")
my_password = os.getenv("PASSWORD")
to_email = os.getenv("TO")

weather_params = WeatherData.generate_data(appid=api_key).model_dump()

p = requests.get(f"{url}/data/2.5/forecast", params=weather_params)
p.raise_for_status()

data_list = json.loads(Weather(p.json()['list']).weather_data())
print(data_list[0]["timestamp"])

notification.send_email_notification(my_email=my_email, my_password=my_password, address="uros.katanic@outlook.com",
                                     message=message.message(date=data_list[0]["timestamp"], current=data_list[0]["current"],
                                                             fill=data_list[0]["feels_like"]))
