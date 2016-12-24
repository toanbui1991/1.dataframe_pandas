# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 10:36:20 2016

@author: User
"""

#how to find and remove duplicate row.
import pandas as pd
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/u.user', sep = '|', header = None, names = user_cols, index_col ='user_id')
users.head()

users.shape
#find the duplicate data form a series.
#there are 148 duplicate zip_code.
users.zip_code.duplicated().sum()
#find the duplicate row.
#the row that is all the same of all features.
users.duplicated().sum()
#find the duplicate row.
users.loc[users.duplicated(), :]
#keep the first record of the duplicate rows.
users.loc[users.duplicated(keep = 'first'), :]
#keep the last record of the duplicate rows.
users.loc[users.duplicated(keep = 'last'), :]
#keep all the duplicated rows.
users.loc[users.duplicated(keep = False), :]


#drops the rows that duplicate>
users.drop_duplicates(keep = 'first').shape

#find the duplicated data with just sub set criteria.
users.duplicated(subset = ['age', 'zip_code']).sum()
#drop_duplicates() to drop duplicates of subset criteries.
users.drop_duplicates(subset = ['age', 'zip_code']).shape

                      
                      