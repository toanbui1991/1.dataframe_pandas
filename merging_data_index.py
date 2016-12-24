# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 15:59:01 2016

@author: User
"""

#Merging on index.
import pandas as pd
import numpy as np
left1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],
                   'value': range(6)})
print(left1)
right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
print(right1)


#you have key column in the left1 and the index in the right1
#'key' column and index of the right1 to be the key.
pd.merge(left1, right1, left_on = 'key', right_index = True)

#you have two data table, left1 and right1 with key column
#and the right_index of the right cloumn. combine these two
#table with left_on = 'key', right_index = 'True', how = 'outer'
pd.merge(left1, right1, left_on = 'key', right_index = True, how = 'outer')


lefth = pd.DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                   'key2': [2000, 2001, 2002, 2001, 2002],
                   'data': np.arange(5.)})
print(lefth)

righth = pd.DataFrame(np.arange(12).reshape((6, 2)),
                   index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
                          [2001, 2000, 2000, 2000, 2001, 2002]],
                          columns=['event1', 'event2'])
print(righth)


#you have two key in the lefth 'key1', 'key2' and 
#hierarical index in right
#left_on = ['key1', 'key2'], right_index = True
#how = 'outer'
pd.merge(lefth, righth, left_on=['key1', 'key2'],
         right_index=True, how='outer')


left2 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]], index=['a', 'c', 'e'],
                  columns=['Ohio', 'Nevada'])
print(left2)

right2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                   index=['b', 'c', 'd', 'e'], columns=['Missouri', 'Alabama'])
print(right2)

#if the key in lef1 and right2 are all index then we have to sepecifed.
#left_index = True, right_index = True
pd.merge(left2, right2, how='outer', left_index=True, right_index=True)



#join can be used more easily if the key linked is index.
left2.join(right2, how='outer')
#link key in left1 is inedex but the linke key on the 
#right1 is 'key' column.
left1.join(right1, on='key')


another = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]],
                    index=['a', 'c', 'e', 'f'], columns=['New York', 'Oregon'])

print(another)
#the key inlink is the index of the two table data.
left2.join([right2, another])

#join multiple data tablw with join
#left2.join([right2, another], how = 'outer')
left2.join([right2, another], how='outer')




