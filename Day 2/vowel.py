# -*- coding: utf-8 -*-
"""
Created on Thu May  9 19:11:55 2019

@author: DELL
"""

state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
vowel=['a','e','i','o','u']

list1=[]
for state in state_name:
    st_element=list(state.lower())
    
    
    for element in vowel:
        while element in  st_element:
            st_element.remove(element)
    list1.append("".join(st_element))
            
print(list1)    