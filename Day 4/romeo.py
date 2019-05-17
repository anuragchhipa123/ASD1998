# -*- coding: utf-8 -*-
"""
Created on Fri May 10 12:23:39 2019

@author: DELL
"""
dict1={}
with open("romeo.txt") as f1:
    for line in f1.readlines():
        list1=line.split()
        for word in list1:
            if word not in dict1:
                dict1[word]=1
                
            else:
                dict1[word]=dict1[word]+1
                
print(dict1)                