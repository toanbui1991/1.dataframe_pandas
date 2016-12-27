# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 11:37:47 2016

@author: User
"""
#Replacing values.
import pandas as pd
import numpy as np
data = pd.Series([1., -999., 2., -999., -1000., 3.])
print(data)

#you can replace the data with replace() method.
#specified what be replace by what
data.replace(-999, np.nan)
#you can also specify a list of number you to replace
data.replace([-999, -1000], [np.nan, 0])

#replace with dictionary
data.replace({-999: np.nan, -1000: 0})
