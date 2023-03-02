'''
多个图以及多个Session
新建一个op时，默认放在默认的图上面
'''
import tensorflow as tf

x = tf.constant(100.0)
y = tf.constant(200.0)
res = tf.add(x,y)
#查看默认的图
graph = tf.get_default_graph()
print('默认的图:',graph)

#新建图
new_graph = tf.Graph()
print('新建的图:',new_graph)

with new_graph.as_default():
    new_op = tf.constant('hello kitty')


with tf.Session(graph=graph) as sess:
    print(sess.run(res))

with tf.Session(graph=new_graph) as sess:
    print(sess.run(new_op))





