'''
变量
变量在run之前，要进行初始化
'''
import tensorflow as tf

#样本数据:(N,3)    第一层神经元数量:5个
init_val = tf.random_normal(shape=[3,5])
w = tf.Variable(init_val)
b = tf.Variable(tf.zeros(shape=(5,)))

#初始化op
init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op) #执行初始化
    ww,bb = sess.run([w,b])
    print(ww)
    print(bb)








