# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:18:42 2019

@author: DELL
"""
from bs4 import BeautifulSoup
import requests
icc="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source=requests.get(icc).text

soup = BeautifulSoup(source,"lxml")
right_table=soup.find('table', class_='table')
print(right_table)
a=[]
b=[]
c=[]
d=[]
e=[]

for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 5:
        a.append(cells[0].text.strip())
        b.append(cells[1].text.strip())
        c.append(cells[2].text.strip())
        d.append(cells[3].text.strip())
        e.append(cells[4].text.strip())


import pandas as pd
from collections import OrderedDict


col_name = ["Pos","Team","Weighted Matches","Points","Rating"]
col_data = OrderedDict(zip(col_name,[a,b,c,d,e]))
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")