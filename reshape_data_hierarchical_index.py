# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 09:25:28 2016

@author: User
"""

#reshaping with hierarchical index.
import pandas as pd
import numpy as np
data = pd.DataFrame(np.arange(6).reshape((2, 3)),
                 index=pd.Index(['Ohio', 'Colorado'], name='state'),
                 columns=pd.Index(['one', 'two', 'three'], name='number'))
print(data)
#using stack and unstack method.
#stack you have a df and you want to create 
#hierarchical index table from row_index, and column_index.
result = data.stack()
print( result)
print(result.unstack)


#you can decide with index should be column index with
#0 or 1 or by name of the index
print(result.unstack(0))
print(result.unstack('state'))


s1 = pd.Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([4, 5, 6], index=['c', 'd', 'e'])
print(s1)
print(s2)
#using concat to build the series with hierarkical index.
data2 = pd.concat([s1, s2], keys = ['one', 'two'])
print(data2)

#unstack the data2, data2 is a series with hierarchical index.
print(data2.unstack())

print(data2.unstack().stack())

print(data2.unstack().stack(dropna=False))


df = pd.DataFrame({'left': result, 'right': result + 5},
              columns=pd.Index(['left', 'right'], name='side'))
print(df)


print(df.unstack('state'))
#summary:
#1.you can convert a df to a series with hierarchical index.
#with stack() method, and change back with unstack().
#you can also control the way of unstack with the column
#0, 1 or the name of the index.
#you can also create a series form two series with concat().
#2.specified the hierarchical index with keys(['one', 'two'])
#3.you can create the df with hierarchical with DataFrame({})
#and change the way the data organize with unstack.





