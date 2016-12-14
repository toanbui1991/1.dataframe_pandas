# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 17:20:28 2016

@author: User
"""

import pandas as pd
movies = pd.read_csv('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/imdb_1000.csv')
#method

print(movies.head())
print(movies.shape)
#filter the data frame base on one criteria with boolean operation.
long_movies = movies[movies['duration'] >= 200]
print(long_movies.head())
print(long_movies.shape)

#get the column value after filter.
print(movies[movies['duration'] >= 200]['title'])
#get the columns value after filter with loc.
#this is the best practice, very easey.
print(movies.loc[movies['duration'] >= 200, 'title'])