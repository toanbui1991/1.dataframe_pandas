# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 20:19:17 2016

@author: User
"""
import pandas as pd
#see the long form of data table, date, item and value columns.
ldata[:10]
#change from long to wide form with pivot() function.
#specified the row_index, and the column index 'date', 'item'
#and the filling value is 'value'
pivoted = ldata.pivot('date', 'item', 'value')
pivoted.head()


#create other column call 'value2'
#np.random.randn to create a normal distribution with mean = 0 u=1,
#you specified the demension of the data.
ldata['value2'] = np.random.randn(len(ldata))
ldata[:10]
#if you just use pivot() method and specified only the 
#row and the column index, 'date', 'item' and the filling value will be other
#columns
pivoted = ldata.pivot('date', 'item')
pivoted['value'][:5]

#the pivot() function is just the same as unstack the 'item'
#change the 'item' from row_index to column index.
#ldata.set_index(['date', 'item']).unstack('item')
unstacked = ldata.set_index(['date', 'item']).unstack('item')





    

