# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 14:21:31 2020

@author: Randhirs
"""
import requests
from pprint import pprint

def by_city():
    city=input('Enter your City name')
    api_url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=437bd602b147a09b5742d9c575622f18&units=metric'.format(city)
    res=requests.get(api_url)
    data=res.json()
    show_data(data)

def show_data(data):
    temperature=data['main']['temp']
    latitute=data['coord']['lat']
    longitude=data['coord']['lon']
    description=data['weather'][0]['description']


    print('Current temprature : {} degree celcius'.format(temperature))
    print('Current latitute : {} '.format(latitute))
    print('Current longitude : {} '.format(longitude))
    print('Current description : {} '.format(description))
    #pprint(data)
    
by_city()
    
