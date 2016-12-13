# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 14:43:31 2016

@author: User
"""

import pandas as pd
#read the tabular data with asumption. tab seperate, the first row is header.
df = pd.read_table('path')
#read the tabular data with the seperator is '|', the first row is data.
#you have to sepecify sep, header = None, names = col_names

col_names = ['user_id', 'age', 'gender', 'accupation', 'zip_code']
df1 = pd.read_table('path', sep = '|', header = None, names = col_names)