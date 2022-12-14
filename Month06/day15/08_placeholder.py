'''
占位符的使用
'''
import tensorflow as tf

plhd = tf.placeholder(tf.float32,[None,3]) #N行3列

data = [[1,2,3],
        [4,5,6],
        [7,8,9]]

#执行占位符时，必须传入具体数据，否则报错
with tf.Session() as sess:
    print(sess.run(plhd,feed_dict={plhd:data}))


