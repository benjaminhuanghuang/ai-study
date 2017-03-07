from __future__ import print_function
from scipy.io import loadmat as load
import matplotlib.pyplot as plt
import numpy as np


def reformat(samples, labels):
    # change data shape
    # (high, width, channel, count ) - > (count, high, width, channel)
    # labels -> one-hot encoding
    # digit 0 represented as 10 , [10] -> [1,0,0,0,0,0,0,0,0,0,0]
    samples = np.transpose(samples, (3, 0, 1, 2))
    labels = np.array([x[0] for x in labels])
    one_hot_labels = []
    for num in labels:
        one_hot = [0.0] * 10
        if num == 10:
            one_hot[0] = 1.0
        else:
            one_hot[num] = 1
        one_hot_labels.append(one_hot)

    labels = np.array(one_hot_labels).astype(np.float32)

    return samples, labels


def normalize(samples):
    pass


def distribution(labels, name):
    pass


def inspect(samples, labels, i):
    print(labels[i])

    plt.imshow(samples[i])
    plt.show()


train_data = load('data/train_32x32.mat')
test_data = load('data/test_32x32.mat')
extra_data = load('data/extra_32x32.mat')

print("Train data samples shape", train_data['X'].shape)
print("Train data Labels shape", train_data['y'].shape)

train_samples = train_data['X']
train_labels = train_data['y']
test_samples = test_data['X']
test_labels = test_data['y']

_train_sample, _train_labels = reformat(train_samples, train_labels)
_test_sample, _test_labels = reformat(test_samples, test_labels)

num_labels = 10
image_size = 32

if __name__ == "__main__":
    inspect(_train_sample, _train_labels, 0)
