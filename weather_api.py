#   API KEY = 04b68b57e46a4aeea1115459241801
# https://www.weatherapi.com/my/
#  http://api.weatherapi.com/v1/current.json?key=04b68b57e46a4aeea1115459241801&q=65203&aqi=no
import requests

_url =  "http://api.weatherapi.com/v1/current.json?key=04b68b57e46a4aeea1115459241801&q=65203&aqi=no"
_response = requests.get(_url)
_weather_json = _response.json()

print(_weather_json)

_tempF = _weather_json.get('current').get('temp_f')
_description = _weather_json.get('current').get('condition').get('text')
_city = _weather_json.get('location').get('name')

print(_tempF, "F")
print("Today's weather in", _city, "is", _description, "and", _tempF, "degrees F")