# -*- coding: utf-8 -*-
"""
Created on Mon May 13 09:09:22 2019

@author: DELL
"""

def pallindrom(x):
    if int(x)>0:
        if x==x[::-1]:
            return True
        
list1=input("Enter the elements : ").split(" ")
print(any(filter(pallindrom,list1)))
