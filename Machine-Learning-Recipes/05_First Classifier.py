'''
https://www.youtube.com/watch?v=AoeEHqVSNOw

'''
import random
from scipy.spatial import distance


# a is train data, b is testing data
def euc(a, b):
    return distance.euclidean(a, b)


class ScrappKNN():
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        predictions = []
        for row in X_test:
            # label = random.choice(self.y_train)
            label = self.closest(row)
            predictions.append(label)

        return predictions

    def closest(self, row):
        best_dist = euc(row, self.X_train[0])
        best_index = 0
        for i in range(1, len(self.X_train)):
            dist = euc(row, self.X_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i
        return self.y_train[best_index]


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
my_classifier = ScrappKNN()
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
