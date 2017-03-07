from __future__ import print_function
from scipy.io import loadmat as load

train = load('data/train_32x32.mat')
print(type(train))

print(train['__version__'])
print(train['__header__'])
print(train['X'])
print(train['X'].shape)  # (32, 32, 3, 73257) (width, height, channel, count)

print(train['y'].shape)  # (73257, 1) (count, data)

print(train['y'][1])