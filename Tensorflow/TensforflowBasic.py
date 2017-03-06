import tensorflow as tf
import numpy as np

hello = tf.constant("Hello, Tensorflow")
session = tf.Session()
print session.run(hello)

session.close()