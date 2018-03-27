from sklearn.cluster import KMeans
from sklearn import datasets

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# dataframes
iris = datasets.load_iris()
samples =[]
model = KMeans(n_clusters=3)
model.fit(samples)
new_samples =[]
labels = model.predict(new_samples)