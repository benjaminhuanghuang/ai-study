# coding: utf-8
from __future__ import print_function
import tensorflow as tf

print("Tensorflow version:", tf.__version__)


def basic_operation():
    v1 = tf.Variable(10)
    v2 = tf.Variable(5)
    addv = v1 + v2
    print(addv)
    print(type(addv))
    print(type(v1))

    c1 = tf.constant(10)
    c2 = tf.constant(5)
    addc = c1 + c2
    print(addc)
    print(type(addc))
    print(type(c1))

    # 用来运行计算图谱的对象/实例？
    # session is a runtime
    sess = tf.Session()

    # Variable -> 初始化 -> 有值的Tensor
    tf.global_variables_initializer().run(session=sess)

    print('变量是需要初始化的')
    print('加法(v1, v2) = ', addv.eval(session=sess))
    print('加法(v1, v2) = ', sess.run(addv))
    print('加法(c1, c2) = ', addc.eval(session=sess))

    # sess2 = tf.Session()
    # with sess2.as_default():
    #     sess2.run(addv)


def use_placeholder():
    graph = tf.Graph()
    with graph.as_default():
        val1 = tf.placeholder(dtype=tf.float64)
        val2 = tf.Variable([3, 4], dtype=tf.fl)


if __name__ == "__main__":
    basic_operation()
