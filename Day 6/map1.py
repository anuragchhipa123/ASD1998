# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:43:02 2019

@author: DELL
"""

import random
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

names=map(lambda x:random.choice(code_names),names)
print(list(names))