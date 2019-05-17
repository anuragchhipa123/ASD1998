# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:19:42 2019

@author: DELL
"""

list1=input("Enter the days :").split(" ")
list2=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for item in list2:
    if item not in list1:
        list1.append(item)
        
print(list1)        