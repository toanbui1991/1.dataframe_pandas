# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 13:54:23 2016

@author: User
"""

#Rename Axis Index.
import pandas as pd
import numpy as np
data = pd.DataFrame(np.arange(12).reshape((3, 4)),
                 index=['Ohio', 'Colorado', 'New York'],
                 columns=['one', 'two', 'three', 'four'])

print(data)

#bring all the index to uppercase.
#data.index will create a series of index,
#then use map to apply str.upper to eache
#element of string.
data.index.map(str.upper)
#now change the index to upper inplace in the data.
data.index = data.index.map(str.upper)
print(data)

#you can also use the rename method to specified
#how to rename the index and columns
data.rename(index = str.upper, columns = str.upper)

#you can specified how rename with a dictionary to mapping
#how to rename the index and column
#index{'OHIO': 'INDIANA'}, columns = {'three': 'peekaboo'}
data.rename(index={'OHIO': 'INDIANA'},
            columns={'three': 'peekaboo'})







