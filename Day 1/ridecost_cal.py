# -*- coding: utf-8 -*-
"""
Created on Tue May  7 20:19:09 2019

@author: DELL
"""

travel = float(input("Enter total kilometers travel in a day: "))
cost = float(input("Enter total cost of diesel per liter: "))
average = float(input("Entre the average of your vehicle: "))
total_cost=(travel/average)*cost
print("total cost of driving per day to office is "+str(total_cost)+" RS")
