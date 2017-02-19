'''
1. Load / Import data
2. Train a classifier
3. Predict label of new one

'''

#
# 1. Import data
#
from sklearn import datasets
from sklearn.cross_validation import train_test_split

iris = datasets.load_iris()
X = iris.data  # features
y = iris.target  # y = f(X)

X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=.5)  # 50% data used for test

#
# 2. Train a classifier
#
from sklearn import tree

my_classifier = tree.DecisionTreeClassifier()
my_classifier.fit(X_train, y_train)

#
# 3. Predict
#
predictions = my_classifier.predict(X_test)
print "expected result ", y_test
print "predicted result ", predictions

#
# Check accuracy
#
from sklearn.metrics import accuracy_score

print accuracy_score(y_test, predictions)
