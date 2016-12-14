# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 00:49:11 2016

@author: User
"""

#read some curtent column with read_csv() method in pandas.
import pandas as pd
df = pd.read_csv('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/ufo.csv')
print(df.columns)


#read the file with some certain columns
df1 = pd.read_csv('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/ufo.csv', usecols = ['City', 'State'])
print(df1.head())
#read the file with some certain columns
df2 = pd.read_csv('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/ufo.csv', usecols = [0, 3])
print(df2.head())

#read some first row to see some data before read the holl big file.
df3 = pd.read_csv('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/ufo.csv', nrows = 5)
print(df3)


#series iteration with pandas data.
for c in df3.City:
    print(c)
    
#iteration through data frame with iterrows() method.

for index, row in df3.iterrows():
    print(index, row.City, row.State)    
    
#the way to drop all the none numeric column value.

drinks = pd.read_csv('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/drinks.csv')
drinks.dtypes
#select all the numeric column with select_dtypes() method and
#specify 
import numpy as np
drinks.select_dtypes(include = [np.number]).dtypes

#use the desribe() method.
#by defualt with will take numberic column oline
#can specified the object typye with include
drinks.describe()
drinks.describe(include = ['object'])
drinks.describe(include = ['object', 'float64'])

