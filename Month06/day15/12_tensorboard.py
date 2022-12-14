'''
将graph中的运算逻辑存入到events事件中，使用tensorboard进行显示
'''
import tensorflow as tf

tensor1d = tf.constant([1,2,3,4,5],name='1d')
var = tf.Variable(tf.random_normal([2,3]),
                  name='varvarvar')

x = tf.constant(100.0,name='xxx')
y = tf.constant(200.0,name='yyy')
res = tf.add(x,y,name='add')

#执行
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    #将sess运行的graph中的信息写入到事件文件
    tf.summary.FileWriter('../summary/',graph=sess.graph)

