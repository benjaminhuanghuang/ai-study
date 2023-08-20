import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Load data
iris_data = load_iris()

features = iris_data.data
feature_names = iris_data.feature_names
target = iris_data.target
target_names = iris_data.target_names

for t in range(3):
    if t == 0:
        c = 'r'
        marker = '>'
    elif t == 1:
        c = 'g'
        marker = 'o'
    elif t == 2:
        c = 'b'
        marker = 'x'
    plt.scatter(features[target == t, 0],
                features[target == t, 1], marker=marker, c=c)
    plt.show()        