# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 10:39:49 2016

@author: User
"""
import pandas as pd
data = pd.DataFrame({'k1': ['one'] * 3 + ['two'] * 4,
                  'k2': [1, 1, 2, 3, 3, 4, 4]})
print(data)
#you can test the duplicated data with
#the duplicated() method
data.duplicated()

#you can drop duplicates row with the method.
#drop_duplicates() by default, the row is duplicates
#if all the value in the row is the same with other row.
data.drop_duplicates()

#you can also specify the criteria, how to be duplicated row.
data['v1'] = [i for i in range(7)]
print(data)
data.drop_duplicates(['k2'])
data.drop_duplicates(['k1', 'k2'], keep = 'last')




