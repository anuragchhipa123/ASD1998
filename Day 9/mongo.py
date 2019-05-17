# -*- coding: utf-8 -*-
"""
Created on Thu May 16 12:00:40 2019

@author: DELL
"""

import pymongo

client = pymongo.MongoClient("mongodb://anuragchhipa:16egccs007%40@cluster0-shard-00-00-fnfn1.mongodb.net:27017,cluster0-shard-00-01-fnfn1.mongodb.net:27017,cluster0-shard-00-02-fnfn1.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

mydb=client.employee


def add_employee(idd, first, last, pay):
    mydb.employees.insert_one(
            {
            "id" : idd,
            "first" : first,
            "last" : last,
            "pay" : pay
            })
    return "Employee added successfully"


def fetch_all_employee():
    user = mydb.employees.find()
    for i in user:
        print (i)
        

add_employee(1,'Sylvester', 'Fernandes',50000)
add_employee(2,'Yogendra', 'Singh', 70000)
add_employee(3,'Rohit', 'Mishra', 30000)
add_employee(4,'Kunal', 'Vaid', 30000)
add_employee(5,'Devendra', 'Shekhawat', 30000)        

fetch_all_employee()