# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 11:15:04 2026

@author: Dell
"""

import pandas as pd
import sqlite3
conn = sqlite3.connect("C:/Users/Dell/Desktop/database/demo3.db")
df = pd.read_sql_query("SELECT * FROM students",conn)
print(df)

#Task1S

import pandas as pd
import sqlite3
conn = sqlite3.connect("C:/Users/Dell/Desktop/internship.db/demo3.db")
df = pd.read_sql_query("SELECT name,track FROM interns",conn)
print(df)
