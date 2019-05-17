# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:23:23 2019

@author: DELL
"""
def leapyear():
    year=int(input("Enter year"))
    if year%100==0:
        if year%400==0:
            print("leap year")
        else:
            print("not a leao year")
    else:
        if year%4==0:
            print("leap year")
        else:
            print("not a leap year")
