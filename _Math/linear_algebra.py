import sys
import numpy as np

print("Python: {}".format(sys.version))
print("Numpy: {}".format(np.__version__))


# define a scalar
x = 6

# define a vector
v = np.array((1, 2, 3))
print("Vector dimensions {}".format(v.shape))
print("Vector size {}".format(v.size))

# define a matrix
m = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrix dimensions {}".format(m.shape))
print("Matrix size {}".format(m.size))


# define a matrix of given dimension
m_ones = np.ones((3, 3, 3))
print("Matrix dimensions {}".format(m_ones.shape))
print("Matrix size {}".format(m_ones.size))

# index
A = np.ones((5,4), dtype= np.int)
A[0,1] = 2
print(A)

# set all rows, second col
A[:,1] = 2   
print(A)

# set all rows, all cols
A[:,:] = 5
print(A)
