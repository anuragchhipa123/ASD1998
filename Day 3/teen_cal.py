# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:39:25 2019

@author: DELL
"""
list1=input("Enter the keys :").split(",")
list2=input("Enter the values").split()
list3=['13','14','17','18','19']
sum=0
d1=dict(zip(list1,list2))
list4=list(d1.values())
a=len(list4)
for i in range(0,a):
    if  list4[i]not in list3:
        sum=sum+int(list4[i])
        
    else:
        continue
    
print(sum)    
        
        
        