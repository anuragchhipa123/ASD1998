# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:23:15 2019

@author: DELL
"""

from functools import reduce
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]
height_total=0
height_count=0
list_filter=list(filter(lambda x:'height' in x,people))
print(list_filter)
list2=list(map(lambda x:x['height'],list_filter))
print(list2)
height_total=reduce(lambda h,w:h+w,list2)
height_count=len(list2)
print("Average = ",height_total / height_count)


