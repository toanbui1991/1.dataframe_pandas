# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 21:46:08 2016

@author: User
"""

import pandas as pd

drinks = pd.read_csv('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/drinks.csv')
drinks.head()
drinks.dtypes

#using groupby() emthod to groupby 'continent'
#using groupby() to sumarize the data.
drinks.beer_servings.mean()
drinks.groupby('continent').beer_servings.mean()
drinks[drinks.continent == 'Africa'].beer_servings.mean()
#using agg to list several aggregate function.
drinks.groupby('continent').beer_servings.agg(['count', 'min', 'max', 'mean'])
drinks[drinks.continent == 'Africa'].mean()


#visualization with pandas and matplotlib
import matplotlib as plt
drinks.groupby('continent').mean().plot(kind = 'bar')
#summary for groupby and aggregate you have.
#mean(), std(),agg([a list of arg]), min(), max(), count() 

