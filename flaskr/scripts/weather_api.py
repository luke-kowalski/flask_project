import requests
from configparser import ConfigParser

parser = ConfigParser()
parser.read("flaskr\config.ini")

API = parser.get("API", "WEATHER_API")

def get_json_data():
    lat = 53.216198
    lon = 19.654487
    api_token = "3af3d3b40ec932ed51b8c87bfecc03d6"
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&exclude=hourly,minutely&appid={API}"

    response = requests.get(url)
    data = response.json()

    return data
