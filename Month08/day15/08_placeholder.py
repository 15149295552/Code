'''占位符
当运行占位符op时，必须为其传入具体数据，否则报错
'''
import tensorflow as tf
import numpy as np
#样本数据
plhd = tf.placeholder('float32',shape=(None,3))#N行3列

data = np.arange(1,10).reshape(3,3)

with tf.Session() as sess:
    print(sess.run(plhd,feed_dict={plhd:data}))





