# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 10:52:05 2016

@author: User
"""

#data tranformation with function or mapping.


import pandas as pd
data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami',
                           'corned beef', 'Bacon', 'pastrami', 'honey ham',
                           'nova lox'],
                   'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

print(data)

#you have a dictionary to mapping the data.
meat_to_animal = {
'bacon': 'pig',
'pulled pork': 'pig',
'pastrami': 'cow',
'corned beef': 'cow',
'honey ham': 'pig',
'nova lox': 'salmon'
}
print(meat_to_animal) 

#create data column called 'animal' and
#use the dictionary to mapping the data.
#in this case the food column
data['animal'] = data['food'].map(str.lower).map(meat_to_animal)
print(data)

#you can also you function to mapping the value.
#this mean for every value in data['food']
#(which is a string), take the method lower.
#then call the value in meat_to_animal
data['animal'] = data['food'].map(lambda x:  meat_to_animal[x.lower()])
print(data)



