from sklearn import datasets
from sklearn.linear_model import LinearRegression

loaded_data = datasets.load_boston()
data_X = loaded_data.data
data_Y = loaded_data.target

model = LinearRegression()
model.fit(data_X, data_Y)  # learn...

print ">> coefficient: ", model.coef_  # 0.1 in y = 0.1x +0.3
print ">> interception: ", model.intercept_  # 0.3 in y = 0.1x +0.3

print ">> Score: ", model.score(data_X, data_Y)
print model.predict(data_X[:4, :])
print data_Y[:4]
