from __future__ import print_function
# https://stackoverflow.com/questions/29433824/unable-to-import-matplotlib-pyplot-as-plt-in-virtualenv
import matplotlib
matplotlib.use('TkAgg') 
from pandas import read_csv
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

url = "https://goo.gl/vhm1eU"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'] 
data = read_csv(url, names=names)

# the distribution data 
description = data.describe()
print(description)

# the dimensions data 
print('The dimensions of data: ', data.shape)
scatter_matrix(data)
plt.show()