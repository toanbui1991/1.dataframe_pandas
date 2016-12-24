# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 10:11:04 2016

@author: User
"""

#database-style dataframe merge.
import pandas as pd
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1': range(7)})
print(df1)
df2 = pd.DataFrame({'key': ['a', 'b', 'd'],
                 'data2': range(3)})
print(df2)

#many to one merge.
#the column with the same name would use
#as the linke (key is in this case)
#get it.
pd.merge(df1, df2)

#it is a good practice to specified the
#key to merge.
#Note: the column with the same name would be used
#as a key, but it is goog practice to specified the key.
pd.merge(df1, df2, on = 'key')

#if the column names are different in each object
#you need to specified it seperately.
#left_on = 'lkey' is the column to link the of df3
#right_one = 'rkey' is the column to link the df4
df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1': range(7)})
df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],
                 'data2': range(3)})
pd.merge(df3, df4, left_on='lkey', right_on='rkey')


#inner join is defualt for the merge function.
#there are other possible option is legt, wright, outer.
#'right' means that key in the wright table would be used.
#'left' means that keys in the left table would be used.
#'inner' intersect of the key.
#'outer' joint set of the key.
print(pd.merge(df1, df2, how = 'left'))
print(pd.merge(df1, df2, how = 'right'))
print(pd.merge(df1, df2, how = 'outer'))



#many to many operation.
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                 'data1': range(6)})
print(df1)
df2 = pd.DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
                       'data2': range(5)})
print(df2)

pd.merge(df1, df2, on='key', how='left')

pd.merge(df1, df2, how='inner')



#merge with multiple key.
left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'],
                  'key2': ['one', 'two', 'one'],
                  'lval': [1, 2, 3]})
print(left)
right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                   'key2': ['one', 'one', 'one', 'two'],
                   'rval': [4, 5, 6, 7]})
print(right)

#you have multiple key like key1 and key2.
pd.merge(left, right, on=['key1', 'key2'], how='outer')
pd.merge(left, right, on = ['key1', 'key2'], how = 'inner')

#if you have two columns with the same name from each table.
#specified the name of each columns with suffixes('_left', '_right')
pd.merge(left, right, on='key1')
pd.merge(left, right, on='key1', suffixes=('_left', '_right'))

 














