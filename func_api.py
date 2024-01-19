# Python 3 Fundamentals, by Sarah Holderness, Pluralsight, 2h 55min
import requests

def people_in_space():
    response = requests.get('http://api.open-notify.org/astros.json')
    json = response.json()
    return json

def degrees_in_F_by_location(inLocationByZip,inApiKey):
    _url =  "http://api.weatherapi.com/v1/current.json?key="+ inApiKey + "&q=" + inLocationByZip + "&aqi=no"
    _response = requests.get(_url)
    _weather_json = _response.json()
    _tempF = _weather_json.get('current').get('temp_f')
    return _tempF