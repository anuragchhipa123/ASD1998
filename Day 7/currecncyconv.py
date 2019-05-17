# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:23:15 2019

@author: DELL
"""
import requests
usd=input("Enter amount:")
url="https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=0fee4fd412577e51a365"
response=requests.get(url)
jsondata=response.json()
#print(jsondata)
print("INR",jsondata['USD_INR']*float(usd))
