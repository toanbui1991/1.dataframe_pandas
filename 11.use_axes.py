# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 01:29:27 2016

@author: User
"""
import pandas as pd
drinks = pd.read_csv('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/drinks.csv')
print(drinks.head())

#drop columns.
drinks.drop('country', axis = 1)
