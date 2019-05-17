# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:06:33 2019

@author: DELL
"""

import re        
str1=input("Enter the emails :").split(",")    
list1=[]
for mail in str1:
    if re.findall('[a-zA-Z0-9-_]*@\w+\.[a-z]{2,4}',mail):
        list1.append(mail)

print (list1)