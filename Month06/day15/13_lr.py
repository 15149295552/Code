'''
使用tensorflow搭建线性回归
'''
import tensorflow as tf
import os

#第一步：数据准备,自己造y=2x + 5
x = tf.random_normal([100,1],mean=1.75,stddev=0.5,name='x_data')
y = tf.matmul(x,[[2.0]]) + 5.0

#第二步：建立模型
#初始化权重（随机数）和偏置（0or1）   wx + b
weight = tf.Variable(tf.random_normal([1,1]),name='w',
                     trainable=True)#训练过程中，是否允许变化
bias = tf.Variable(0.0,name='b',trainable=True)
#预测值
pred_y = tf.matmul(x,weight) + bias

#第三步：损失函数（均方误差）
loss = tf.reduce_mean(tf.square(y - pred_y))

#第四步：梯度下降，求损失函数极小值
train_op = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

#收集损失函数的值
tf.summary.scalar('losses',loss)
megred = tf.summary.merge_all()

#模型保存对象
saver = tf.train.Saver()

#执行
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())#执行初始化
    #打印初始的权重和偏置
    print('weight:{},bias:{}'.format(weight.eval(),bias.eval()))

    #文件写入对象
    fw = tf.summary.FileWriter('../summary/',graph=sess.graph)

    #在开始训练之前，检查是否已经有模型保存了，如果有，则加载
    if os.path.exists('../model/LinearRegression/checkpoint'):
        saver.restore(sess,'../model/LinearRegression/')

    #循环训练
    for i in range(100):
        sess.run(train_op)
        #执行一次梯度下降，损失值就有变化，变化一次，收集一次
        summary = sess.run(megred)
        fw.add_summary(summary,i)
        print('轮数:{},weight:{},bias:{}'.format(i+1,
                                                 weight.eval(),
                                                 bias.eval()))

    #训练完成，保存模型
    saver.save(sess,'../model/LinearRegression/')