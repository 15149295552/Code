'''
线性回归
'''
import tensorflow as tf

#数据准备(样本数据)
x = tf.random_normal([100,1],mean=1.75,stddev=0.5)
y = tf.matmul(x,[[2.0]]) + 5.0

#构建模型 y = wx + b
#初始化模型参数
init_val = tf.random_normal(shape=(1,1))
w = tf.Variable(init_val,trainable=True)
b = tf.Variable(0.0,trainable=True)
pred_y = tf.matmul(x,w) + b
#损失函数:均方误差
loss = tf.reduce_mean(tf.square(y - pred_y))
#梯度下降优化器
train_op = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

#收集损失函数的值
tf.summary.scalar('losses',loss)
megred = tf.summary.merge_all()
#定义模型保存、加载对象
saver = tf.train.Saver()

#开始训练
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    #开始训练之前，打印模型初始化参数
    print('w:{},b:{}'.format(w.eval(),b.eval()))

    #文件写入对象
    fw = tf.summary.FileWriter('../summary/',graph=sess.graph)

    for i in range(500):
        sess.run(train_op)
        summary = sess.run(megred)
        fw.add_summary(summary,i+1)
        print('轮数:{},w:{},b:{}'.format(i+1,w.eval(),b.eval()))
    #训练完成之后，保存模型
    saver.save(sess,'../model/lr/')
    print('模型保存成功')





