'''
转换张量的类型
'''
import tensorflow as tf

ones = tf.ones(shape=(2,3),dtype='int32')
temp = tf.cast(ones,'float32')
zeors = tf.zeros(shape=(2,3),dtype='float32')

#浮点型和字符串不能转换
with tf.Session() as sess:
    print(temp.eval())
    # print(sess.run(tf.cast(zeors,tf.string))) #报错





