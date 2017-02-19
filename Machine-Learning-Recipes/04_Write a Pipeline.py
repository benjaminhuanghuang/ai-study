'''
https://www.youtube.com/watch?v=84gqSbLcBFE

def classify(X)   # features
    # do some logic  <- Learning
    return y # label


playground.tensorflow.org
'''

from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()

X = iris.data  # features
y = iris.target  # y = f(X)

X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=.5)  # 50% data used for test

#
#  Case 1
#
from sklearn import tree

my_classifier = tree.DecisionTreeClassifier()

my_classifier.fit(X_train, y_train)
predictions = my_classifier.predict(X_test)
print "expected result ", y_test
print "predicted result ", predictions

print accuracy_score(y_test, predictions)

#
#  Use KNeighborsClassifier
#
from sklearn.neighbors import KNeighborsClassifier

my_classifier = KNeighborsClassifier()

my_classifier.fit(X_train, y_train)
predictions = my_classifier.predict(X_test)
print "expected result ", y_test
print "predicted result ", predictions

print accuracy_score(y_test, predictions)
