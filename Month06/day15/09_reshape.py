'''
张量的形状改变
静态形状：初始形状，不能跨介设置，固定下来就不能改变
'''
import tensorflow as tf

plhd = tf.placeholder('float32',[None,3])
#设置静态形状
print(plhd)
plhd.set_shape([4,3]) #固定下来
print(plhd)
# plhd.set_shape([3,4])  保存，固定下来不允许修改

#动态形状,可以设置多次，跨介设置
new_plhd = tf.reshape(plhd,[1,4,3])
# print(new_plhd)
# print(plhd)

new_plhd2 = tf.reshape(new_plhd,[1,1,4,3])
print(new_plhd2)

#运行
with tf.Session() as sess:
    pass