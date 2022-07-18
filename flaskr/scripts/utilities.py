import requests
from datetime import date
from configparser import ConfigParser

parser = ConfigParser()
parser.read("flaskr\config.ini")

API = parser.get("API", "WEATHER_API")


def get_json_data():
    lat = 53.216198
    lon = 19.654487
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&exclude=hourly,minutely&appid={API}"

    response = requests.get(url)
    data = response.json()

    return data


def get_footer_time():
    return date.today().year

