'''
手写体识别:全连接神经网络
'''
import pylab
import os
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# 下载数据
mnist = input_data.read_data_sets('../MNIST_data/',
                                  one_hot=True)

# 定义占位符
x = tf.placeholder('float32', shape=[None, 784])
y = tf.placeholder('float32', shape=[None, 10])

# 搭建模型
w = tf.Variable(tf.random_normal(shape=(784,10)))
b = tf.Variable(tf.zeros(shape=(10,)))
pred_y = tf.nn.softmax(tf.matmul(x, w) + b)
# 损失函数:交叉熵
cross_entropy = -tf.reduce_sum(y * tf.log(pred_y), reduction_indices=1)
cost = tf.reduce_mean(cross_entropy)
# 梯度下降优化器
train_op = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

model_save_path = '../model/mnist/'
saver = tf.train.Saver()
batch_size = 100  # 批次大小

# 运行
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#
#     # 开始训练之前，检查是否有模型保存
#     if os.path.exists('../model/mnist/checkpoint'):
#         saver.restore(sess, model_save_path)
#
#     for epoch in range(100):  # 外层循环控制轮数
#         # 计算总批次
#         total_batch = int(mnist.train.num_examples / batch_size)
#         total_cost = 0.0
#         for i in range(total_batch):  # 内层循环控制批次数
#             train_x, train_y = mnist.train.next_batch(batch_size)
#             params = {x: train_x, y: train_y}
#             o, c = sess.run([train_op, cost],
#                             feed_dict=params)
#             total_cost += c
#         avg_cost = total_cost / total_batch
#         print('轮数:{},cost:{}'.format(epoch + 1, avg_cost))
#     print('训练结束')
#
#     # 模型的评估(准确率)
#     corr = tf.equal(tf.argmax(y, 1), tf.argmax(pred_y, 1))
#     accuracy = tf.reduce_mean(tf.cast(corr, 'float32'))
#     acc = sess.run(accuracy, feed_dict={x: mnist.test.images,
#                                         y: mnist.test.labels})
#     print('测试集准确率:',acc)
#     #保存模型
#     saver.save(sess,model_save_path)

#拿到2张图像，进行测试
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    #加载模型
    saver.restore(sess,model_save_path)
    #从测试集中读取两张图像
    test_x,test_y = mnist.test.next_batch(2)

    pred_val = sess.run(pred_y,feed_dict={x:test_x})
    print('真实类别:', tf.argmax(test_y, 1).eval())
    print('预测类别:',tf.argmax(pred_val,1).eval())
    print('预测概率:',tf.reduce_max(pred_val,1).eval())

    #显示图片
    img1 = test_x[0].reshape(28,28)
    pylab.imshow(img1)
    pylab.show()

    img2 = test_x[1].reshape(28,28)
    pylab.imshow(img2)
    pylab.show()






