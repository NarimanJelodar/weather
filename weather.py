import os
import requests
from dotenv import  load_dotenv
from pprint import pprint
def get_current_weather(city = 'Tehran' ):
    load_dotenv()
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric"

    weather_data = requests.get(request_url).json()
    return  weather_data 


if __name__  == "__main__":
    pprint(get_current_weather())
