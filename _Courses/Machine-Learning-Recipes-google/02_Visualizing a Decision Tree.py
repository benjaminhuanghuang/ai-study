'''
https://www.youtube.com/watch?v=tNa99PG8hR8&spfreload=5

Types of classifiers:
    Artificial neural network
    Support Vector Machine
    Lions
    Tigers
    Bears

Goals:
    1. Import dataset
    2. Train a classifier
    3. Predict label of new flower

Requirements:
brew install graphviz
'''

from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree

#
#  Import data
#
iris = load_iris()
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
print iris.feature_names

print iris.target_names  # ['setosa' 'versicolor' 'virginica']

print iris.data[0]  # [ 5.1  3.5  1.4  0.2]
print iris.target[0]  # 0 setosa

for i in range(len(iris.target)):
    print "Example {}: label {}, features {}".format(i, iris.target[i], iris.data[i])

#
# Training
#
# training data
test_idx = [0, 50, 100]
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

# testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

#
# Predict label for new flower
#
print "expected result:", test_target
print "predicted result: ", clf.predict(test_data)

#
# Visualize
#
from sklearn.externals.six import StringIO
import pydotplus

dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data,
                     feature_names=iris.feature_names,
                     class_names=iris.target_names,
                     filled=True,
                     rounded=True,
                     impurity=False)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf('iris.pdf')

print test_data[0], test_target[0]
print iris.feature_names, iris.target_names