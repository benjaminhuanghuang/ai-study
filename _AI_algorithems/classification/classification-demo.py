from __future__ import print_function
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import sklearn
import pandas as pd
import numpy as np
import seaborn as sns # statistical data visualization



# Uing Car evaluation data set
# https://archive.ics.uci.edu/ml/datasets/car+evaluation
names = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'eval']
df = pd.read_table('https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data', sep=',', names = names)

print ('car count:', df['eval'].value_counts())
car_counts['Percentage'] = car_counts['eval'] / car_counts.sum()[0]