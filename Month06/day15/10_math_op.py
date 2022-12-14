'''
张量的数学计算
'''
import tensorflow as tf

x = tf.constant([[1,2],
                 [3,4]],dtype='float32')
y = tf.constant([[4,3],
                 [2,1]],dtype='float32')

add = tf.add(x,y)
mul = tf.matmul(x,y)
log_x = tf.log(x)
sum_x = tf.reduce_sum(x,axis=0)

#片段和
data =     tf.constant([1,2,3,4,5,6,7,8,9],dtype='float32')
segement = tf.constant([0,0,0,1,1,1,2,2,2],dtype='int32')
res = tf.segment_sum(data,segement)

with tf.Session() as sess:
    print(add.eval())
    print(mul.eval())
    print(log_x.eval())
    print(sum_x.eval())
    print(res.eval())


