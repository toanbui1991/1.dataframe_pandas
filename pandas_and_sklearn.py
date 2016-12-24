# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 10:09:00 2016

@author: User
"""
import os
import pandas as pd
os.getcwd()
train = pd.read_csv('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/titanic_train.csv')
train.head()
train.shape
train.columns
#create feature matrix X.
feature_cols = ['Pclass', 'Parch']
X = train.loc[:,feature_cols]
X.shape
#create target vector y.
y = train.Survived
y.shape

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X, y)

test = pd.read_csv('C:/Users/User/Desktop/DataScience/1.dataframe_pandas/data/titanic_test.csv')
X_news = test.loc[:, feature_cols]
X_news.shape

new_pred_class = logreg.predict(X_news)

#create a csv file from the pandas object.
pd.DataFrame({'PassengerId': test.PassengerId, 'Prediction': new_pred_class}).set_index('PassengerId').to_csv('sub.csv')

print(new_pred_class)
print(test.PassengerId)
