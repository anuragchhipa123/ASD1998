# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:44:03 2019

@author: DELL
"""


import sqlite3
from pandas import DataFrame

conn = sqlite3.connect ( 'db_University.db' )

c = conn.cursor()


c.execute ("""CREATE TABLE students(
          roll INTEGER,
          name  TEXT,
          branch TEXT,
          age INTEGER
          )""")



c.execute("INSERT INTO students VALUES (01,'Sylvester', 'CSE', 23)")
c.execute("INSERT INTO students VALUES (02,'Yogendra', 'IT', 23)")
c.execute("INSERT INTO students VALUES (03,'Pradeep', 'ECE', 22)")
c.execute("INSERT INTO students VALUES (04,'Kunal', 'ECE', 22)")
c.execute("INSERT INTO students VALUES (05,'Devendra', 'ME', 23)")
c.commit()

c.execute("SELECT * FROM students")
data=list(c.fetchone())


df = DataFrame(c.fetchall())

df.columns = ["roll","name","branch","age"]


