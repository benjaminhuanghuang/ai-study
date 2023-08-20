'''
    Introduction to Machine Learning with Python Ch1
    k-Nearest Neighbors
        To make a prediction for a new data point, the algorithm
    finds the point in the training set that is closest to the new point. Then it assigns the
    label of this training point to the new data point.

    - https://github.com/amueller/introduction_to_ml_with_python
    
'''
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Load data
iris_dataset = load_iris()

# Explor the data
print("Keys of iris_dataset: \n{}".format(iris_dataset.keys()))

# print the short description 'DESCR'
print(iris_dataset['DESCR'][:193] + "\n...")

print("Target names: {}".format(iris_dataset['target_names']))
print("Feature names: \n{}".format(iris_dataset['feature_names']))

print("Type of data: {}".format(type(iris_dataset['data'])))
print("Shape of data: {}".format(iris_dataset['data'].shape))

print("Type of target: {}".format(type(iris_dataset['target'])))  # 1d array
print("Shape of target: {}".format(iris_dataset['target'].shape))
# 0 means setosa, 1 means versicolor, and 2 means virginica.
print("Target:\n{}".format(iris_dataset['target']))

print("Type of data: {}".format(type(iris_dataset['data'])))


# shuffles the dataset using a pseudo-random number generator
# 75% for training and 25% for test
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0)

# create dataframe from data in X_train
# label the columns using the strings in iris_dataset.feature_names
iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset['feature_names'])
# create a scatter matrix from the dataframe, color by y_train
pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o',
                           hist_kwds={'bins': 20}, s=60, alpha=.8)
# plt.show()

# All machine learning models in scikit-learn are called Estimator.
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)  
print(knn)

knn.fit(X_train, y_train)

# Making predictions
X_new = np.array([[5, 2.9, 1, 0.2]])
prediction = knn.predict(X_new)
print("Prediction: {}".format(prediction))
print("Predicted target name: {}".format(
    iris_dataset['target_names'][prediction]))

# Evaluating the model
y_pred = knn.predict(X_test)
print("Test set score: {:.2f}".format(np.mean(y_pred == y_test)))  
print("Test set score2: {:.2f}".format(knn.score(X_test, y_test)))