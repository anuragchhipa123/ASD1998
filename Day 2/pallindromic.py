# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:50:01 2019

@author: DELL
"""

list1=input("Enter the element in list").split(" ")
print(list1)
for l1 in list1:
    if (int(l1)<0):
        ans="false"
        break
    elif(int(l1)<10):
        ans="true"
        break
        
    elif (l1==l1[::-1]):
        ans="true"
        break
    else:
        ans="false"
print(ans)