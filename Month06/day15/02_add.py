'''
张量相加
'''
import tensorflow as tf

#定义
x = tf.constant(100.0)
y = tf.constant(200.0)
res = tf.add(x,y)

#执行
with tf.Session() as sess:
    print(sess.run(res))

