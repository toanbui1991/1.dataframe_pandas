# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 01:29:27 2016

@author: User
"""
#note: the axis specify where operation take place.
#0 mean row, 1 mean column
import pandas as pd
drinks = pd.read_csv('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/drinks.csv')
print(drinks.head())

#drop columns.
drinks.drop('country', axis = 1).head()
#drop row,
drinks.drop([2], axis = 0).head()

#compute mean of each columns.
#axis = 0 mean operate on row,
#ore row colapse
drinks.mean(axis = 0).shape
#mean of each row.
drinks.mean(axis = 1).shape

