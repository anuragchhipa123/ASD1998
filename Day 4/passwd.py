# -*- coding: utf-8 -*-
"""
Created on Fri May 10 13:01:39 2019

@author: DELL
"""
dict1={}
with open("passwd") as f1:
    for line in f1.readlines():
        list1=line.split(":")
        if list1[0]=="#":
            continue
        else:
            dict1[list1[0]]=list1[2]
new_name = list(sorted(dict1))
for new in new_name:
    print(new,dict1[new])
        
        