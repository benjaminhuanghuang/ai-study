from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

loaded_data = datasets.load_boston()
data_X = loaded_data.data
data_Y = loaded_data.target

model = LinearRegression()
model.fit(data_X, data_Y)  # learn...

print model.predict(data_X[:4, :])
print data_Y[:4]

# Generate training data
X, y = datasets.make_regression(n_samples=1000, n_features=1, n_targets=1, noise=10)
plt.scatter(X, y)
plt.show()
