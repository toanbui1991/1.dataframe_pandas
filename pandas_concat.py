# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 17:03:45 2016

@author: User
"""

#Concatenating along an Axix.
import numpy as np
import pandas as pd

#using concatenate() method to concatenate data df.
arr = np.arange(12).reshape((3, 4))
print(arr)

np.concatenate([arr, arr], axis=1)
s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])

pd.concat([s1, s2, s3])

pd.concat([s1, s2, s3], axis=1)

s4 = pd.concat([s1 * 5, s3])
pd.concat([s1, s4], axis=1)
#you have two data table to cancat and you you to 
#concat in cloumn and just take the inner index.
#[s1, s4], axis = 1, join = 'inner'
pd.concat([s1, s4], axis=1, join='inner')
#you just want to join specific valueof the indexs.
#join_axes = [['a', 'c', 'b', 'e']]
pd.concat([s1, s4], axis=1, join_axes= [['a', 'c', 'b', 'e']])

#you want to create a hierachical index with string concat
#the level of each series concat is keys = ['one', 'two', 'three']
result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])
result

#the keys = ['one', 'two', 'three'] become columns header.
pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three'])


df1 = pd.DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'],
                columns=['one', 'two'])
print(df1)

df2 = pd.DataFrame(5 + np.arange(4).reshape(2, 2), index=['a', 'c'],
                columns=['three', 'four'])
print(df2)
#hierachical column index for each df.
#keys ['level1', 'level2']
pd.concat([df1, df2], axis=1, keys=['level1', 'level2'])
#get the same result
pd.concat({'level1': df1, 'level2': df2}, axis=1)


#get the name the each level of the columns index
#names = ['upper', 'lower']
pd.concat([df1, df2], axis=1, keys=['level1', 'level2'],
          names=['upper', 'lower'])



df1 = pd.DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd'])
print(df1)
df2 = pd.DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'])
print(df2)

#the index is not important then you set
#ignore_index = True. Do not preserve,
#ndexes along concatenation axis, instead producing a new
#range(total_length) index
#the index will be reconstruct with the length of row.
pd.concat([df1, df2], ignore_index=True)









