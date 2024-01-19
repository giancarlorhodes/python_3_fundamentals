# Python 3 Fundamentals, by Sarah Holderness, Pluralsight, 2h 55min
#import requests
import func_api

#response = requests.get('http://api.open-notify.org/astros.json')
#json = response.json()

#print(json)
_json = func_api.people_in_space()


for person in _json['people']:
    print(person['name'])