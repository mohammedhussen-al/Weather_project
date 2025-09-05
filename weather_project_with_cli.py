
#   https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
#https://api.openweathermap.org/data/3.0/onecall?
# lat={lat}&   
# lon={lon}&
# exclude={part}&
# appid={your Api key openweathermap.org} 
#   http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}

# http://api.openweathermap.org/geo/1.0/direct?q=
# {city name}, jinput
# {state code},
# {IQ}&  first IQ then we add input
# limit={limit}&
# appid={your Api key openweathermap.org} it is free

# gui

 
    
import json
import requests

def set_url(city_):
    return f"https://api.openweathermap.org/geo/1.0/direct?q={city_},IQ&limit=1&appid={your Api key openweathermap.org}"

def get_url(lat,lon):
    return f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={your Api key openweathermap.org}&units=metric"

def func(lat,lon):
    weather =requests.get(get_url(lat,lon))
    if weather:
        weather = weather.json()
        data = weather["main"]
        #print(weather["main"])
        print(f"Temp: ",end="") 
        print(data["temp"],end="")
        print("c*")
        print(f"Feels like: ",end="")
        print(data["feels_like"],end="")
        print("c*")
        print(f"Humidity: ",end="")
        print(data["humidity"],end="")
        print("%")
city_ = input("enter city name: ")
city_ = city_.lower()
city_ = city_.capitalize()
url = set_url(city_)

responses = requests.get(url)

if responses.status_code == 200:
    res = responses.json()
    if res:
        city = res[0]
        func(lat=city["lat"],lon=city["lon"])


