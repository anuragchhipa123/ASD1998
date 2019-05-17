# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:17:44 2019

@author: DELL
"""
import csv
with open("zoo.csv","rt") as f1:
    print(f1.readlines())
    
dict1={}    
with open("zoo.csv") as f1: 
    
    csv_reader = csv.reader(f1)
    next(csv_reader)
    for row in csv_reader:
        if  row[0] in dict1:
            dict1[row[0]]=dict1[row[0]]+1
        else:
            dict1[row[0]]=1
        
print(dict1)



dict1={}    
with open("zoo.csv") as f1: 
    
    csv_reader = csv.reader(f1)
    next(csv_reader)
    for row in csv_reader:
        if  row[0] in dict1:
            dict1[row[0]]=int(dict1[row[0]])+dict1[row[0]]
        else:
            dict1[row[0]]=int(row[2])
        
print(dict1)
    