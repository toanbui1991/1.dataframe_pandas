# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 09:56:19 2016

@author: User
"""

import pandas as pd
drinks = pd.read_csv('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/drinks.csv')
drinks.head()
drinks.dtypes

#indes
drinks.index
#columns.
drinks.columns
drinks.shape

user = pd.read_table('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/u.user',
                     sep = '|', header = None)
print(user.head())

#index is the id for rows.
drinks[drinks.continent == 'South America']

#get the value with index and columns name.
drinks.loc[23, 'beer_servings']

#set reset the index manually.
drinks.set_index('country', inplace = True)
drinks.head()

drinks.shape
drinks.columns
drinks.index

drinks.loc['Brazil', 'beer_servings']

#get the name of the index.
drinks.index.name
#set the index name to None.
drinks.index.name = None
print(drinks.head())
#get the index name back.
#and make the index as a columns.
drinks.index.name = 'country'
drinks.reset_index(inplace = True)
drinks.head()

#summary: given use have a column that can change to index.
#ob.set_index('col_name')
#given you have a df with index have name.
#ob.reset_index(inplace = True)

drinks.describe()
drinks.describe().index
drinks.describe().columns
#interact with the object result of an object.
drinks.describe().loc['25%', 'beer_servings']



