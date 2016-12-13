# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 15:09:01 2016

@author: User
"""

import pandas as pd
#pd.read_csv to read the csv file with assumption that the first row is header.
df = pd.read_csv('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/ufo.csv')
#want to see type of the object, in this case data frame.
type(df)
#see the first five row of the data fame.
df.head() 
#get the series City.
city = df['City']
print(type(city))
#create new series in the df.
df['Location'] = df['City'] + ', ' + df['State']
print(df.head())
print(df.shape)
