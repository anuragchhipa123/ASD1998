# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:09:59 2019

@author: DELL
"""
import requests
str1=input("Enter the city name:")
url1="http://api.openweathermap.org/data/2.5/weather"
url2="?q="+str1
url3="&appid=c93ac84a2172d10664ecaba211097d21"
url=url1+url2+url3
print(url)

response = requests.get(url)
response.content
jsondata = response.json()
print(jsondata)
print("longitude:",jsondata['coord']['lon'])
print("latitude:",jsondata['coord']['lat'])
print("Weather:",jsondata['weather'][0]['main'])
print("Wind Speed:",jsondata['wind']['speed'])
print("Sunset:",jsondata['sys']['sunset'])
print("Sunrise:",jsondata['sys']['sunrise'])