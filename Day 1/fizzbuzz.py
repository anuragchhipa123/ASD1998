# -*- coding: utf-8 -*-
"""
Created on Tue May  7 22:46:02 2019

@author: DELL
"""

n=0
while(n<101):
    n=n+1
    if n%3==0 and n%5==0:
        print("fizzbuzz")
        continue
    elif n%3==0:
        print("fizz")
        continue
    elif n%5==0:
        print("buzz")
        continue
    print(n)
      