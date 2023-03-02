'''
张量的形状改变
静态形状:不能跨介设置，固定下来就不能改变了
动态形状:可以跨介设置，可以设置多次
'''
import tensorflow as tf

plhd = tf.placeholder('float32',shape=[None,3])
#设置静态形状
print(plhd)
plhd.set_shape([2,3])
print(plhd)
# plhd.set_shape([3,2]) #报错

#动态形状
new_plhd = tf.reshape(plhd,(1,2,3))
print(new_plhd)





