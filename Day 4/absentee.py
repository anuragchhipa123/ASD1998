# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:04:58 2019

@author: DELL
"""
with open("absentee.txt" , "wt") as ab:
    count=25
    while True:
        if count==0:
            break
        else:
            name=input("Enter the student name")
            ab.write(name+"\n")
            count=count-1
            if not name:
                break
with open("absentee.txt" ,"rt") as ab:
    for item in ab.readlines():
        print(item)
        
    
    
    