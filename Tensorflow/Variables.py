import tensorflow as tf

state = tf.Variable(5, name="counter")

one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)

# add init op to the graph
init_op = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init_op)
    print sess.run(state)

    for _ in range(3):
        sess.run(update)
        print sess.run(state)