'''
将graph中的op存入事件文件，并在tensorboard中显示
'''
import tensorflow as tf

x = tf.constant(100.0,name='xxx')
y = tf.constant(200.0,name='yyy')
add = tf.add(x,y,name='add')

with tf.Session() as sess:
    print(sess.run(add))
    #创建文件写入对象
    tf.summary.FileWriter('../summary/',graph=sess.graph)



