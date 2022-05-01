import requests
import bot

def getWeather(name):
    req = requests.get('http://api.weatherapi.com/v1/current.json?key=0157db8d19ee40a683092035220105&q=' + str(name))
    if('error' in req.json()):
        return req.json()['error']
    else:
        return req.json()['current']