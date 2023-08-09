import numpy as np

A = np.matrix([[1,2], [3,4]])
B = np.ones((2,2), dtype=np.int)

C = A + B
print(C)

C = A * B
print(C)


# transpose
A = np.array(range(9))
A = A.reshape(3,3)
print(A)

B = A.T
print(B)
