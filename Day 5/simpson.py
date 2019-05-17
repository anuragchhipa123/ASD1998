# -*- coding: utf-8 -*-
"""
Created on Sat May 11 12:47:32 2019

@author: DELL
"""

import re
with open("simpsons_phone_book.txt","rt")as fp1:
    for contect in fp1.readlines():
        if re.findall('^[jJ]{1}\w*\s+Neu',contect):
            print(contect)
        