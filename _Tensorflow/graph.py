import tensorflow as tf
import numpy as np

matrix1 = tf.constant([[3.], [3.]])
matrix2 = tf.constant([[1., 2.]])

product = tf.matmul(matrix1, matrix2)

sess = tf.Session()
print sess.run(product)

sess.close()

# sesson case 2
with tf.Session() as sess:
    result = sess.run(product)
    print result


# session case 3
sess = tf.InteractiveSession()
x = tf.Variable([1.0, 2.0])
a = tf.constant([3.0, 3.0])

# init x using the run() method
x.initializer.run()

sub = tf.sub(x, a)
print sub.eval()
sess.close()


