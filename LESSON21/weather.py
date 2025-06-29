import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def getCurrWeather_():
    print('\n*** Get Current Weather Condition ***\n')

    city = input('\nPlease enter a city name:\n').replace(' ', '_')

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    print(request_url)

    weather_data = requests.get(request_url).json()
    pprint(weather_data)

    print('\n\n\n')

    print(f'\nCurrent weather for {weather_data["name"]}')
    print(f'\nThe temp is {weather_data["main"]["temp"]}')
    print(f'\nFeels like {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"]}.')

    print('\n\n\n')

if __name__ == '__main__':
    getCurrWeather_()