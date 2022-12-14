'''
默认的图
'''
import tensorflow as tf

x = tf.constant(100.0)
y = tf.constant(200.0)
res = tf.add(x,y)

#获取默认的图
graph = tf.get_default_graph()
print('默认的图:',graph)

with tf.Session() as sess:
    print(sess.run(res))
    print(x.graph)
    print(y.graph)
    print(res.graph)