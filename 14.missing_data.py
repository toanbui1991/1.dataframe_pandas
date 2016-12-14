# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 22:25:46 2016

@author: User
"""

import pandas as pd
ufo = pd.read_csv('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/ufo.csv')
#isnull() method is a data frame method.
ufo.tail()
ufo.isnull().tail()
ufo.notnull().tail()

#there are how many nan value for each column.
#using isnull() and sum()
ufo.isnull().sum()

#data filter with city is nan
ufo[ufo.City.isnull()]

#dropna() 
ufo.shape
ufo.dropna(how = 'any').shape
ufo.dropna(how = 'all').shape

ufo.dropna(subset = ['City', 'Shape Reported'], how = 'any').shape
ufo.dropna(subset = ['City', 'Shape Reported'], how = 'all').shape  

#value_counts() method default with dropna = True           
ufo['Shape Reported'].value_counts()           
ufo['Shape Reported'].value_counts(dropna = False)
ufo['Shape Reported'].fillna(value = 'VARIOUS', inplace = True)
ufo['Shape Reported'].value_counts(dropna = False)
