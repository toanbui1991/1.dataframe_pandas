# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 10:47:31 2016

@author: User
"""

import pandas as pd
#read the tab sperated data table with read_table() method.
orders = pd.read_table('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/chipotle.tsv')
print(orders.head())
print(orders.dtypes)

#use the string method in pandas object.
#upper case for all 'item_name'.
#str method upper()
print(orders.item_name.str.upper())
#use str method contains()
#this is boolean operation
print(orders.item_name.str.contains('Chicken'))
#use boolean operation str.contains to filter
print(orders[orders.item_name.str.contains('Chicken')])


print(orders.choice_description.head())
#you want to remove [] from 'choice_description'
orders.choice_description.str.replace('[', '').head(10)
orders.choice_description.str.replace('[', '').str.replace(']', '').head(10)


