# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:18:14 2019

@author: DELL
"""
import string
a_z = string.ascii_lowercase + string.ascii_uppercase
count=0
str1=input("Enter the string:")
a=len(str1)
if len(str1)<26:
    print("not pangrama" )
else:
    for i in range(0,a):
        str2=str1.lower()
    for j in range(0,26):
        if(a_z[j]in str2):
            count=count+1
            continue
        else:
            break
        
           
        