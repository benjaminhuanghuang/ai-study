from numpy import *

random.rand(4, 4)

# mat()convert an array to a matrix
randMat = mat(random.rand(4, 4))

# inverse a matrix
invRandMat = randMat.I

myEye = randMat * invRandMat

# eye(4)creates an identity matrix of size 4.
myEye - eye(4)
