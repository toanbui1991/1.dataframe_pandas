# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 16:13:29 2016

@author: User
"""

import pandas as pd
movies = pd.read_csv('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/imdb_1000.csv')
#method

print(movies.head())
print(movies.describe())
#describe the columns which are not number type.
print(movies.describe(include = ['object']))
#attribute

print(movies.shape)
print(movies.dtypes)