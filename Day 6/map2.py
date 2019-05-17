# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:11:34 2019

@author: DELL
"""

names = ['Mary', 'Isla', 'Sam']
names=map(lambda x:hash(x),names)
print(list(names))