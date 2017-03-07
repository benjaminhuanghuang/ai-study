from __future__ import print_function
from scipy.io import loadmat as load

train = load('data/train_32x32.mat')
print(type(train))

print(train['__version__'])
print(train['__header__'])
print(train['X'])
print(train['X'].shape)