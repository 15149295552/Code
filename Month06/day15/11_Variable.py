'''
变量：模型参数
'''
import tensorflow as tf

init_val = tf.random_normal([4,5])
w = tf.Variable(init_val)
b = tf.Variable([0,0,0,0,0])

#初始化op
init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op) #初始化op不能使用eval执行
    print(sess.run([w,b]))