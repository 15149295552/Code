'''
执行两个张量的相加
'''
import tensorflow as tf

x = tf.constant(100.0)
y = tf.constant(200.0)
res = tf.add(x,y)

with tf.Session() as sess:
    res = sess.run(res)
    print(res)









