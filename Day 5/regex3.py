# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:41:17 2019

@author: DELL
"""
import re
list1=[]
while True:
    str1=input("Enter the card number ")
    list1.append(str1)
    
    if  not str1:
        break
for num in list1:
    if re.findall('[4-6]{1}[0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}',num):
        print("Valid")
        
    else:
        print("Invalid")
    