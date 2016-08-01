#!/usr/bin/env python

import pandas as pd
from pandasql import *

df1 = pd.read_csv('Advertising.csv')

#sale type, value 
# this table would be "better" structured as medium (i.e. tv, newspaper, etc) + value - more what i'm used to 

# I don't know why you do this 
pysqldf = lambda q: sqldf(q, globals())

# That should work...not sure why it doesn't seem to
tv = pysqldf('SELECT round(tv/10,0)*10 AS tv_value ,count(1) AS num FROM df1 GROUP BY tv_value ORDER BY tv_value ASC LIMIT 100')

#tv = ps.sqldf(q2, locals())

tv.head()

tv.to_csv('tv_agg2.csv')

# df.pivot_table

# Global vars 

"""
import csv
with open('Advertising.csv') as csvfile;
    reader = csv.DictRedaer (csvfile)w
    for row in reader:
    	print(row['TV'], row['Radio']) # can print only if it meets a certain condition 
    	# like the where clause 
    	if row.salesperson == 'Erica' sum(row['TV'])


def my_function():
	a = 3 # local vairable
	print 'hi'

# global and local - retur
# outside this function"""