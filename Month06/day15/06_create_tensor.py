'''
创建张量
'''
import tensorflow as tf

tensor1d = tf.constant([1,2,3,4,5])

tensor2d = tf.constant([[1,2,3],
                        [4,5,6]])

zeros = tf.zeros(shape=[2,3],dtype='float32')
ones = tf.ones(shape=[2,3],dtype=tf.float32)
#随机正态分布
tensornd = tf.random_normal(shape=[10],#维度
                            mean=0,#期望值
                            stddev=1,#标准差
                            dtype='float32')

#执行
with tf.Session() as sess:
    print('结果为:{}'.format(tensor1d.eval()))
    print(tensor2d.eval())
    print(zeros.eval())
    print(ones.eval())
    print(tensornd.eval())