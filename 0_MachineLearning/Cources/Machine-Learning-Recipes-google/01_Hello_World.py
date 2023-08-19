'''
https://www.youtube.com/watch?v=cKxRvEZd3Mw&t=32s

Supervised Learning:  Create a classifier by finding patterns in examples
    1.  Collect training data
    2.  Train classifier
    3.  Make predictions

Training data
'''

from  sklearn import tree

'''
# input
features = [
    [140, "smooth"],
    [130, "smooth"],
    [150, "bumpy"],
    [170, "bumpy"]
]

# output
labels = ["apple", "apple", "orange", "orange"]
'''

features = [
    [140, 1],
    [130, 1],
    [150, 0],
    [170, 0]
]

# output
labels = [0, 0, 1, 1]
# classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)  # training
print clf.predict([150, 0])  # 150 , bumpy  return orange
