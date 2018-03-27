'''
    DataCamp-Machine Learning with Python
    https://campus.datacamp.com/courses/supervised-learning-with-scikit-learn/classification?ex=4

    Exploratory data analysis (EDA) in order to understand the structure of the data. 
        UCI Machine Learning Repository : https://archive.ics.uci.edu/ml/datasets/Congressional+Voting+Records
'''

from sklearn import datasets
import pandas as pd
import numpy as np

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/voting-records/house-votes-84.data')

print('Data', df.head())
print('Data info', df.info())
print('Data description', df.describe())
