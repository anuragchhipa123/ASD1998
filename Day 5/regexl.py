# -*- coding: utf-8 -*-
"""
Created on Sat May 11 09:09:45 2019

@author: DELL
"""
import re
str1=input("Enter the string:").split(",")
for num in str1:
    if re.findall('[+-.]?[0-9]*\.[0-9]+',num):
        print("yes")
        
    else:
        print("no")
