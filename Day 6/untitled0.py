# -*- coding: utf-8 -*-
"""
Created on Mon May 13 19:46:50 2019

@author: DELL
"""
import csv
from collections import defaultdict

with open("population.csv","rt") as f1:
    print(f1.readlines())
    
dict1={}
with open("population.csv") as f1:    
    csv_reader = csv.reader(f1)
    next(csv_reader)
    for row in csv_reader:
        if  row[3] in dict1:
            dict1[row[3]]=dict1[row[3]]+1
        else:
            dict1[row[3]]=1
        
print(dict1)



dict1={  }    
with open("population.csv") as f1: 
    
    csv_reader = csv.reader(f1)
    next(csv_reader)
    for row in csv_reader:
        if  row[3] in dict1:
            dict1[row[3]]=int(dict1[row[3]])+dict1[row[3]]
        else:
            dict1[row[3]]=int(row[0])
        
print(dict1)