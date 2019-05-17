# -*- coding: utf-8 -*-
"""
Created on Thu May 16 12:25:27 2019

@author: DELL
"""

from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS

import pymongo

client = pymongo.MongoClient("mongodb://anuragchhipa:16egccs007%40@cluster0-shard-00-00-fnfn1.mongodb.net:27017,cluster0-shard-00-01-fnfn1.mongodb.net:27017,cluster0-shard-00-02-fnfn1.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
mydb=client.employee

#url = "http://keralaresults.nic.in/sslc2018rgr8364/swr_sslc.htm"
url = "https://bidplus.gem.gov.in/bidlists"
"""//*[@id="pagi_content"]/div[1]/div[1]/p[1]/a
//*[@id="pagi_content"]/div[2]/div[1]/p[1]/a
//*[@id="pagi_content"]/div[1]/div[2]/p[1]/strong
//*[@id="pagi_content"]/div[2]/div[2]/p[1]/strong
//*[@id="pagi_content"]/div[2]/div[2]/p[2]/strong
//*[@id="pagi_content"]/div[3]/div[2]/p[2]/strong
//*[@id="pagi_content"]/div[1]/div[3]/p[1]/strong
//*[@id="pagi_content"]/div[2]/div[3]/p[1]/strong
"""

browser = webdriver.Chrome("D:\Forsk\chromedriver_win32\chromedriver.exe")
browser.get(url)


sleep(2)

A=[]
B=[]
C=[]
D=[]

for i in range(1,11):
    A.append(browser.find_element_by_xpath("//*[@id='pagi_content']/div["+str(i)+"]/div[1]/p[1]/a").text)    
    B.append(browser.find_element_by_xpath("//*[@id='pagi_content']/div["+str(i)+"]/div[2]/p[1]/span").text)
    C.append(browser.find_element_by_xpath("//*[@id='pagi_content']/div["+str(i)+"]/div[2]/p[2]/span").text)
    D.append(browser.find_element_by_xpath("//*[@id='pagi_content']/div["+str(i)+"]/div[3]/p[1]").text)


sleep(5)

def add_item(A, B, C, D):
    for i in range(1,10):
        mydb.employees.insert_one(
            {
            "asd" : A[i],
            "pdt" : B[i],
            "qwe" : C[i],
            "dept" : D[i]
            })
    return "Employee added successfully"


def fetch_all_item():
    user = mydb.employees.find()
    for i in user:
        print (i)
        
add_item(A,B,C,D)
fetch_all_item()        
 
html_page = browser.page_source

soup = BS(html_page)


sleep(3)


browser.quit()
