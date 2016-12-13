# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 14:43:31 2016

@author: User
"""

import pandas as pd
#read the tabular data with asumption. tab seperate, the first row is header.
df = pd.read_table('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/chipotle.tsv')
#read the tabular data with the seperator is '|', the first row is data.
#you have to sepecify sep, header = None, names = col_names
df.head()
df.shape
df.columns.values

col_names = ['user_id', 'age', 'gender', 'accupation', 'zip_code']
df1 = pd.read_table('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/u.user', sep = '|', header = None, names = col_names)
print(df1.head())
print(df1.shape)