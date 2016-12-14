# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 00:05:16 2016

@author: User
"""

import pandas as pd
movies = pd.read_csv('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/imdb_1000.csv')
#method
#filter with one criteria
print(movies.head())
print(movies.shape)
long_movies = movies[movies['duration'] >= 200]
print(long_movies.head())
print(long_movies.shape)

#filter with multiple criteria.
print(movies[(movies.duration >= 200) & (movies.genre == 'Drama')])
print(movies[(movies['duration'] >= 200) & (movies['genre'] == 'Drama')])
movies['duration'] >= 200 & movies['genre'] == 'Drama'

#multiple criteria with or |
print(movies[(movies.duration >= 200) | (movies.genre == 'Drama')])

#this multiple criteria make more sense.
print(movies[(movies.genre == 'Crime') | (movies.genre == 'Drama') | (movies.genre == 'Action')])
