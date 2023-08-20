# -*- coding: utf-8 -*-
'''
深度学习基础介绍 机器学习 6 6 决策树应用
https://www.youtube.com/watch?v=WidVNMsXz4E&list=PLO5e_-yXpYLARtW5NPHTFVYY-xpgwuNNH&index=6
'''

from sklearn.feature_extraction import DictVectorizer  # convert category to int as 1,0
import csv
from sklearn import preprocessing
from sklearn import tree  # decision tree
from sklearn.externals.six import StringIO

DEBUG = True

allElectronicsData = open("allelectronics.csv", 'rb')
reader = csv.reader(allElectronicsData)
headers = reader.next()
if DEBUG:
    print headers

featureList = []  # list of dict
labelList = []  # last column of the data
for row in reader:
    labelList.append(row[-1])
    rowDict = {}
    for i in range(1, len(row) - 1):
        rowDict[headers[i]] = row[i]

    featureList.append(rowDict)
if DEBUG:
    print featureList

# Convert data
vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()
print "dummyX:", dummyX
print vec.get_feature_names()

print "labelList:", str(labelList)

lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print "dummyY:", str(dummyY)

clf = tree.DecisionTreeClassifier(criterion='entropy')  # ID3
clf = clf.fit(dummyX, dummyY)  # Training
print "clf: ", str(clf)

with open("allElectronicsInfomaitonGainOri.dot", 'w') as f:
    f = tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file=f)

oneRowX = dummyX[0, :]
print "oneRowX: ", str(oneRowX)
newRowX = oneRowX
newRowX[0] = 1
newRowX[2] = 0
print "newRowX: ", str(newRowX)

predictedY = clf.predict(newRowX)
print "predictedY: " + str(predictedY)
