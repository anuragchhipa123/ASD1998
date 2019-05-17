# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:19:59 2019

@author: DELL
"""

str1=input("Enter the string : ")
dict1={}
for i in str1:
    if  i in dict1:
        dict1[i]=dict1[i]+1
    else:
        dict1[i]=1
print(dict1)       