# -*- coding: utf-8 -*-
"""
Created on Fri May 10 09:17:22 2019

@author: DELL
"""
"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy.py
  Problem Statement:
    Make a program that create a copy of a file    
"""
with open("word.txt" , "rt") as rs:
    with open("word2.txt" ,"wt") as ws:
        for line in rs:
            ws.write(line)
