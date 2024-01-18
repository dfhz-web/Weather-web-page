import requests
from dotenv import load_dotenv
import os  # we need to call the api from the .env
from pprint import pprint # for beauty when printing json from the api

#it is gonna load in those environments variables, so we can retrieve them
load_dotenv()  #This line initializes the process of loading environment variables from the .env file, and allows to use os.getenv

def get_current_weather(city="Pereira"):
    #we modify the url , and it kinda different from the documentation 
   
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
    request_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_KEY")}&units=metric'
    weather_data = requests.get(request_url).json()
    return weather_data



    # print(request_url)
    #json is the way data is sent  back and forth for many many applications
    
    # pprint(weather_data)

    # print(f'\nCurrent weather for {weather_data["name"]}')
    # print(f'\nThe temp in Celsius  {weather_data["main"]["temp"]}')
    # print(f'\nFeels like  {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"]}.')



if __name__ == "__main__":
    print('\n***Get current WEather Condition ***\n')
    city = input("\nPlease enter a city name: ")

   #check for empty string or string with only spaces
    #only works when sending nothing, or sending spaces
    if not bool(city.strip()):
        city = "Pereira"


    weather = get_current_weather(city)
    print("\n")
    pprint(weather)