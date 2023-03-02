'''
创建张量示例
'''
import tensorflow as tf
import numpy as np

tensor1d = tf.constant([1,2,3,4,5])
tensor2d = tf.constant(np.arange(1,10).reshape(3,3))
zeros = tf.zeros(shape=(2,3),dtype='float32')
ones = tf.ones(shape=(2,3),dtype=tf.float32)
tensornd = tf.random_normal(shape=(10,),
                            mean=1.75,
                            stddev=0.1,
                            dtype='float32')
#截尾正态分布
tensor_trun = tf.truncated_normal(shape=(10,),
                                  mean=1.75,
                                  stddev=0.1)

with tf.Session() as sess:
    print(tensor1d.eval())
    print(tensor2d.eval())
    print(zeros.eval())
    print(ones.eval())
    print(tensornd.eval())
    print(tensor_trun.eval())

