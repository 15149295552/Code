'''
张量类型的转换
'''
import tensorflow as tf

ones = tf.ones(shape=[3,3],dtype='int32')
zeros = tf.zeros(shape=[3,3],dtype='float32')
#类型转换
temp = tf.cast(ones,'float32')
# temp1 = tf.cast(zeros,tf.string) #字符串和浮点型之间不能转换

#执行
with tf.Session() as sess:
    print(sess.run(temp))
    # print(sess.run(temp1))