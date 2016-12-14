# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 11:09:25 2016

@author: User
"""

import pandas as pd
drinks = pd.read_csv('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/drinks.csv')
print(drinks.head())
print(drinks.dtypes)

#change the data type of a columns with astype() method.
drinks['beer_servings'] = drinks.beer_servings.astype(float)
print(drinks.dtypes)

#change the data type of a column in the reading statage with read_csv.
drinks1 = pd.read_csv('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/drinks.csv',
                      dtype = {'beer_servings' : float})
print(drinks1.dtypes)

orders = orders = pd.read_table('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/chipotle.tsv')
print(orders.head())
print(orders.dtypes)

orders.item_price.str.replace('$', '').astype(float).mean()


