'''
TensorFlow for Poets
TF Learn : High level ML library on top of TensorFlow

'''

from sklearn import metrics, cross_validation
import tensorflow as tf
from tensorflow.contrib import learn


def main(unused_argv):
    iris = learn.datasets.load_dataset('iris')
    X_train, X_test, y_train, y_test = \
        cross_validation.train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

    classifier = learn.DNNClassifier(hidden_units=[10, 20, 10], n_classes=3)

    classifier.fit(X_train, y_train, steps=200)
    score = metrics.accuracy_score(y_test, classifier.predict(X_test))
    print "Accuracy: {0:f}".format(score)
