# -*- coding: utf-8 -*-
"""
Created on Fri May 10 12:54:56 2019

@author: DELL
"""

str1=input("Enter the file name")

with open("romeo.txt") as f1:
    f1.seek(0,0)
    com=f1.readlines()
    print(com[-1])