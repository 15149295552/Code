'''
手写体识别
模型：全连接神经网络
'''
import os
import pylab
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# 定义样本读取对象
mnist = input_data.read_data_sets('../MNIST_data/',
                                  one_hot=True)  # 独热编码

# 数据准备
x = tf.placeholder(tf.float32, [None, 784])  # N行784列
y = tf.placeholder(tf.float32, [None, 10])  # N行10列

# 定义权重，偏置
w = tf.Variable(tf.random_normal([784, 10]))
b = tf.Variable(tf.zeros([10]))

# 构建模型
pred_y = tf.nn.softmax(tf.matmul(x, w) + b)
# 损失函数,交叉熵
cross_entropy = -tf.reduce_sum(y * tf.log(pred_y), reduction_indices=1)
cost = tf.reduce_mean(cross_entropy)
# 梯度下降
train_op = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

# 模型保存对象
saver = tf.train.Saver()
batch_size = 100

# 执行
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())  # 初始化
#
#     if os.path.exists('../model/mnist/checkpoint'):
#         saver.restore(sess, '../model/mnist/')
#
#     # 开始训练
#     for epoch in range(50):  # 轮数
#         total_batch = int(mnist.train.num_examples / batch_size)
#
#         total_cost = 0.0
#         for i in range(total_batch):  # 批次
#             # 拿到一个批次的数据
#             train_x, train_y = mnist.train.next_batch(batch_size)
#             params = {x: train_x, y: train_y}
#             op, c = sess.run([train_op, cost],
#                              feed_dict=params)
#             total_cost += c
#         avg_cost = total_cost / total_batch
#         print('轮数:{},cost:{}'.format(epoch + 1, avg_cost))
#     print('训练结束.....')
#
#     # 模型评估: 精度  ＝ 对的个数/总个数
#     corr = tf.equal(tf.argmax(y, 1),  # 真实类别
#                     tf.argmax(pred_y, 1))  # 预测类别
#     # 将corr布尔值转为浮点型
#     accuracy = tf.reduce_mean(tf.cast(corr, tf.float32))
#     acc = accuracy.eval({x: mnist.test.images,
#                          y: mnist.test.labels})
#     print('accuracy:',acc)
#
#     # 保存模型
#     saver.save(sess, '../model/mnist/')


# 从测试集中,随机读取2张图像,执行预测

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    # 加载模型
    saver.restore(sess, '../model/mnist/')

    # 从测试集中随机拿到两个样本
    test_x, test_y = mnist.test.next_batch(2)

    pred_val = sess.run(pred_y,
                        feed_dict={x: test_x})

    print('真实类别:',sess.run(tf.argmax(test_y,1)))
    print('预测类别:',sess.run(tf.argmax(pred_val,1)))
    print('预测概率:',sess.run(tf.reduce_max(pred_val,axis=1)))

    #显示图像
    img = test_x[0]
    img1 = img.reshape(28,28)
    pylab.imshow(img1)
    pylab.show()

    img = test_x[1]
    img2 = img.reshape(28, 28)
    pylab.imshow(img2)
    pylab.show()


