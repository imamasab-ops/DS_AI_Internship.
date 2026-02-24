# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 12:38:42 2026

@author: Dell
"""
#task1

import pandas as pd
import sqlite3
conn = sqlite3.connect("C:/Users/Dell/Desktop/internship.db/demo3.db")
df = pd.read_sql_query(" SELECT track, AVG(stipend) AS average_stipend FROM interns GROUP BY track",conn)
df1 = pd.read_sql_query(" SELECT track, COUNT(*) AS total_interns FROM interns GROUP BY track",conn)
df2 = pd.read_sql_query("  SELECT track, COUNT(*) AS total_interns, AVG(stipend) AS average_stipend FROM interns GROUP BY track",conn)
print(df)
print(df1)
print(df2)


#task2
import sqlite3
import pandas as pd
# Connect to database
conn = sqlite3.connect("C:/Users/Dell/Desktop/internship.db/demo3.db")
# Define JOIN query
query = """
SELECT 
    i.name AS intern_name,
    i.track,
    m.mentor_name
FROM interns i
INNER JOIN mentors m
    ON i.track = m.track;
"""
# Load into Pandas DataFrame
df = pd.read_sql_query(query, conn)
# Display results
df.head()
