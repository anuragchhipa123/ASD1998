# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:20:18 2019

@author: DELL
"""

str1=input("Enter the string : ")

count1=0
count2=0
for i in str1:
    if i.isalpha():
        count1=count1+1
        
    elif i.isdigit():
        count2=count2+1
        
    else:
        continue
    
print(count1)
print(count2)    