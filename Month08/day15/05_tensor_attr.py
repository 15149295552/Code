'''
张量的基本属性
'''
import tensorflow as tf

x = tf.constant(100.0,dtype='float32',name='xxx')

with tf.Session() as sess:
    print(sess.run(x))
    print('name:',x.name)
    print('shape:',x.shape)
    print('dtype:',x.dtype)
    print('graph:',x.graph)
    print('op:',x.op)