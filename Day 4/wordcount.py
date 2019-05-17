# -*- coding: utf-8 -*-
"""
Created on Fri May 10 21:56:53 2019

@author: DELL
"""
file1=("Enter the file name : ")

with open("romeo.txt") as f1:
    lines=0
    words=0
    characters=0
    for line in f1:
        list1=line.split()
        lines=lines+1
        words=words+len(list1)
        characters+= sum(len(word) for word in list1)
print(lines)
print(words)
print(characters)        
        
    
    
        