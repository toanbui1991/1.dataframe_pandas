# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 22:08:15 2016

@author: User
"""
import matplotlib as plt
import pandas as pd
movies = pd.read_csv('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/imdb_1000.csv')
movies.head()
movies.dtypes
#use desribe() mehod for object type (usually string)
movies.genre.describe()
#use value_counts() method to mave more information about series.
movies.genre.value_counts()
#specify the normalize = True to give percentage of each type.
movies.genre.value_counts(normalize = True)
type(movies.genre.value_counts())
#this is a series ==> you can use series method.
movies.genre.value_counts().head()
#find unique values with unique method.
movies.genre.unique()

#use crosstab() method to build the matrix table.

pd.crosstab(movies.genre, movies.content_rating)

#use describe() method for numeric column.
movies.duration.describe()

#data visualization for numeric columns
movies.duration.plot(kind = 'hist')

#summary to explore a series you have 
#describe(), value_counts(), mean(), unique()..