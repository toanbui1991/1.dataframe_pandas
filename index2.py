# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 10:17:05 2016

@author: User
"""

import pandas as pd
drinks = pd.read_csv('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/drinks.csv')
drinks.head()
drinks.dtypes

drinks.continent.head()

drinks.set_index('country', inplace = True)
drinks.head()
drinks.continent.head()

drinks.continent.value_counts()

drinks.continent.value_counts().values
#index the series
drinks.continent.value_counts().loc['Africa']

drinks.continent.value_counts().sort_index()
#sort_index() vs sort_values
drinks.continent.value_counts().sort_values()

