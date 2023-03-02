'''
张量的一些数学计算
'''
import tensorflow as tf

x = tf.constant([[1,2],
                 [3,4]],dtype='float32')
y = tf.constant([[1,2],
                 [3,4]],dtype='float32')
add = tf.add(x,y)
mul = tf.matmul(x,y)
log = tf.log(x)
sum_x = tf.reduce_sum(x,axis=1)

data = tf.constant([1,2,3,4,5,6,7,8,9])
ids =  tf.constant([0,0,0,1,1,1,2,2,2])
segment_sum = tf.segment_sum(data,ids)

with tf.Session() as sess:
    print(add.eval())
    print(mul.eval())
    print(log.eval())
    print(sum_x.eval())
    print(segment_sum.eval())




