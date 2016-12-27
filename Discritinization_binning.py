# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 14:13:24 2016

@author: User
"""

#Discritinization and Binning.
import pandas as pd
import numpy as np

#you can create discrete variable from a list of value
#and a list of range, the result will be this be value
#is what bin.
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
print(cats)
#the labels attribute bill let us the the order of the bin
#of each value bin.
cats.labels
#the levels attribute will let us see the unique level of the bins.
cats.levels

#the value_counts() function will count the number each bin in the data.
pd.value_counts(cats)

#by defualt the will cut fromt right like (18, 25]
#but you can reverse it with right = False
pd.cut(ages, [18, 26, 36, 61, 100], right=False)

#you can also assign the name for each bin with labels attribute.
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
pd.cut(ages, bins, labels=group_names)


data = np.random.rand(20)
#if you dont specify the bins with a list
#and instead is a number pd.cut() wil devided 
#the data into n bin equal by min and max value.
pd.cut(data, 4, precision=2)

#you can also use the pd.qcut() function to cut by quantitle.
data = np.random.randn(1000) # Normally distributed
cats = pd.qcut(data, 4) # Cut into quartiles
cats
pd.value_counts(cats)

#you can also specify the quantitle with a list
#[0, 0.1, 0.5, 0.9, 0.1]
cat1 = pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.])
cat1.levels
cat1.value_counts()
cat1.labels








