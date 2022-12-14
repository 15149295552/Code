'''
多个图，多个Session
新增的OP，只能添加到默认的图上。
临时拿到默认的图的权限
'''
import tensorflow as tf

x = tf.constant(100.0)
y = tf.constant(200.0)
res = tf.add(x,y)

graph = tf.get_default_graph()
print('默认的图:',graph)

#新建一个图
new_graph = tf.Graph()
print('新建的图:',new_graph)
#临时将新图，设为默认的图
with new_graph.as_default():
    new_op = tf.constant('hello world')


#执行
with tf.Session(graph=graph) as sess:
    print(sess.run(res))

with tf.Session(graph=new_graph) as sess1:
    print(sess1.run(new_op))



