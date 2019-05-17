# -*- coding: utf-8 -*-
"""
Created on Sat May 11 12:33:25 2019

@author: DELL
"""



import re        
str1=input("Enter the emails :").split(",")    
list1=[]
for mail in str1:
    if re.findall('[a-zA-Z0-9-_]*@\w+\.[a-z]{2,4}',mail):
        list1.append(mail)
list1.sort()
for i in list1:        
    print (i)