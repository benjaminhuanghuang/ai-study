from __future__ import print_function

import sklearn
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn import linear_model

# Load data into DataFrame
data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
col_names = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE",
             "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT", "MEDV"]
'''
There are 14 attributes in each case of the dataset. They are:

    CRIM - per capita crime rate by town
    ZN - proportion of residential land zoned for lots over 25,000 sq.ft.
    INDUS - proportion of non-retail business acres per town.
    CHAS - Charles River dummy variable (1 if tract bounds river; 0 otherwise)
    NOX - nitric oxides concentration (parts per 10 million)
    RM - average number of rooms per dwelling
    AGE - proportion of owner-occupied units built prior to 1940
    DIS - weighted distances to five Boston employment centres
    RAD - index of accessibility to radial highways
    TAX - full-value property-tax rate per $10,000
    PTRATIO - pupil-teacher ratio by town
    B - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
    LSTAT - % lower status of the population
    MEDV - Median value of owner-occupied homes in $1000's
'''
df = pd.read_csv(data_url, delimiter=r"\s+", names=col_names)
print(df.head())  # retrun fist n rows, default n = 5
print(df.shape)  # dimensionality of the DataFrame

X = df[["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE", "DIS","RAD","TAX","PTRATIO","B","LSTAT"]]
y = df[['MEDV']]

# Slice data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=5)

# Train model
reg = linear_model.LinearRegression()  # import the linear model
reg.fit(X_train, y_train)

# Predict
reg.predict([[0.03237, 0.0, 2.18, 0,0.458, 6.998, 45.8, 6.0622, 3,222.0,18.7, 394.63, 2.94]])
print( 'The intercept is', reg.intercept_)
print( 'The slops are', reg.coef_)

print ('the predict result is', reg.predict([[0.03237, 0.0, 2.18, 0,0.458, 6.998, 45.8, 6.0622, 3,222.0,18.7, 394.63, 2.94]]))

# Check accuracy
y_pred = reg.predict(X_test)
y_test_m = y_test.as_matrix()

plt.figure(figsize=(15,10))
plt.plot(y_test_m, ms=50, alpha=1)
plt.plot(y_pred, ms=50, alpha=1)
legend_list =['y_test_m','y_pred']
plt.legend(legend_list, loc=4, fontsize='25')

from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
print( 'The mean_squared_error is', mean_squared_error(y_test, y_pred))
print( 'The score is', r2_score(y_test, y_pred))

