# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 16:30:12 2016

@author: User
"""

import pandas as pd
#pd.read_csv to read the csv file with assumption that the first row is header.
df = pd.read_csv('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/ufo.csv')
#see some data and the name of columns
print(df.head())
print(df.columns)
print(df.shape)

#change the name of the column with the remane method.
#inplace = True because you want the operation in the underline data.
df.rename(columns = {'Colors Reported' : 'Colors_Reported', 'Shape Reported' : 'Shape_Reported'}, inplace = True)
print(df.columns)

#rename the columns name by assign the new list of value.
col_names = ['city', 'colors reported', 'shape reported', 'state', 'time']
df.columns = col_names
print(df.columns)

#rename the columns names in the reading stage.
#header = 0, the first row is header.
#names = col_names to assign the new names.
df1 = pd.read_csv('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/ufo.csv', names = col_names, header = 0)
print(df1.columns)

#replace the columns name which have space with under score.
df1.columns = df1.columns.str.replace(' ', '_')
print(df1.columns)
