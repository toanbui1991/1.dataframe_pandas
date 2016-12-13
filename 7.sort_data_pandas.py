# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 17:04:33 2016

@author: User
"""

import pandas as pd
movies = pd.read_csv('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/imdb_1000.csv')
#method

print(movies.head())

#sort the values of series with sort_values method.
type(movies['title'].sort_values())
movies['title'].sort_values()
movies['title'].sort_values(ascending = False)
#sort the data frame with sort_values method base one a key
#key in this case is 'title' column
movies.sort_values('title')
movies.sort_values('duration').head()
movies.sort_values('duration', ascending = False).head()

#sorting the data frame with multiple key.
movies.sort_values(['content_rating', 'duration'], ascending = False)
