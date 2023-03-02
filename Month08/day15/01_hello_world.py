import tensorflow as tf

#定义
hello = tf.constant('hello world')

#执行
sess = tf.Session()
res = sess.run(hello)
print(res)
sess.close()