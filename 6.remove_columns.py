# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 16:45:43 2016

@author: User
"""

import pandas as pd
#pd.read_csv to read the csv file with assumption that the first row is header.
df = pd.read_csv('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/ufo.csv')
#see some data and the name of columns
print(df.head())
print(df.shape)

#remove the columns with drop method.
df.drop('Colors Reported', axis = 1, inplace = True)
print(df.head())
#delete a list of columns with drop method.
df.drop(['City', 'State'], axis = 1, inplace = True)
print(df.head())
#delete a list of row with drop method.

df.drop([0, 1], axis = 0, inplace = True)
#you delete the index 0 and 1
print(df.head())
print(df.shape)


