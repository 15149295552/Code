'''
使用卷积神经网络实现服饰识别
'''
import tensorflow as tf
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets


class FashionMnist:
    out_feature1 = 12  # 第一层的卷积输出通道数(第一层的卷积核数量)
    out_feature2 = 24  # 第二层的卷积输出通道数(第二层的卷积核数量)
    con_neurons = 512  # 第一个全连接的神经元数量

    def __init__(self, path):
        self.data = read_data_sets(path,
                                   one_hot=True)
        self.sess = tf.Session()

    def close(self):
        self.sess.close()

    def init_weight_var(self, shape):
        # 截尾正态分布
        init_val = tf.truncated_normal(shape, mean=0.0, stddev=0.1)
        return tf.Variable(init_val)

    def init_bias_var(self, shape):
        init_val = tf.constant(1.0, shape=shape)
        return tf.Variable(init_val)

    def conv2d(self, x, w):
        '''
        :param x: 输入数据
        :param w: 卷积核
        :return:
        '''
        return tf.nn.conv2d(x,  # 输入数据
                            w,  # 卷积核
                            strides=[1, 1, 1, 1],  # 样本数量,高度,宽度,通道数
                            padding='SAME')  # 同维卷积

    def max_pool_2x2(self, x):
        return tf.nn.max_pool(x,  # 输入数据
                              ksize=[1, 2, 2, 1],  # 池化区域
                              strides=[1, 2, 2, 1],  # 池化步长
                              padding='SAME')

    def create_conv_pool_layer(self, input, input_feature, out_feature):
        '''
        卷积池化组
        :param input: 输入数据
        :param input_feature: 输入通道数
        :param out_feature: 输出通道数
        :return:
        '''
        filter_w = self.init_weight_var([5, 5, input_feature, out_feature])
        b_conv = self.init_bias_var([out_feature])
        h_conv = tf.nn.relu(self.conv2d(input, filter_w) + b_conv)
        h_pool = self.max_pool_2x2(h_conv)

        return h_pool

    def create_fc_layer(self, h_pool_flat, input_feature, con_neurons):
        '''
        全连接层
        :param h_pool_flat: 输入数据
        :param input_feature: 输入特征数量
        :param con_neurons: 神经元数量
        :return:
        '''
        w_fc = self.init_weight_var([input_feature, con_neurons])
        b_fc = self.init_bias_var([con_neurons])
        h_fc1 = tf.nn.relu(tf.matmul(h_pool_flat, w_fc) + b_fc)

        return h_fc1

    def build(self):
        '''
        组建CNN
        :return:
        '''
        # 数据准备
        self.x = tf.placeholder(tf.float32, shape=[None, 784])
        x_image = tf.reshape(self.x, [-1, 28, 28, 1])
        self.y = tf.placeholder(tf.float32, [None, 10])

        # 搭建网络
        # 第一组卷积池化
        h_pool1 = self.create_conv_pool_layer(x_image, 1, self.out_feature1)
        # 第二组卷积池化
        h_pool2 = self.create_conv_pool_layer(h_pool1,
                                              self.out_feature1,
                                              self.out_feature2)
        # 第一个全连接
        h_pool2_flat_features = 7 * 7 * self.out_feature2
        h_pool2_flat = tf.reshape(h_pool2, [-1, h_pool2_flat_features])
        h_fc = self.create_fc_layer(h_pool2_flat,
                                    h_pool2_flat_features,
                                    self.con_neurons)
        # 丢弃层
        h_fc1_drop = tf.nn.dropout(h_fc, 0.5)

        # 输出层
        w_fc = self.init_weight_var([self.con_neurons, 10])  # 512,10
        b_fc = self.init_bias_var([10])
        pred_y = tf.matmul(h_fc1_drop, w_fc) + b_fc

        # 损失函数(先计算softmax,再计算交叉熵)
        loss = tf.nn.softmax_cross_entropy_with_logits(labels=self.y,  # 真实值
                                                       logits=pred_y)  # 预测值
        cross_entropy = tf.reduce_mean(loss)

        # 梯度下降,自适应梯度下降
        self.train_op = tf.train.AdamOptimizer(0.0001).minimize(cross_entropy)

        # 准确率
        corr = tf.equal(tf.argmax(self.y, 1),
                        tf.argmax(pred_y, 1))

        self.accuracy = tf.reduce_mean(tf.cast(corr, tf.float32))

    def train(self):
        '''
        训练模型
        :return:
        '''
        self.sess.run(tf.global_variables_initializer())
        batch_size = 100
        print('开始训练.......')

        for i in range(50):
            total_batch = int(self.data.train.num_examples / batch_size)

            for j in range(total_batch):
                train_x, train_y = self.data.train.next_batch(batch_size)
                params = {self.x: train_x, self.y: train_y}
                o, acc = self.sess.run([self.train_op, self.accuracy],
                                       feed_dict=params)

                if j % 100 == 0:
                    print('轮数:{},批次:{},acc:{}'.format(i, j, acc))

    def metrics(self):
        test_x,test_y = self.data.test.next_batch(100)
        params = {self.x: test_x, self.y: test_y}
        test_acc = self.sess.run(self.accuracy,
                                 feed_dict=params)
        print('Test acc:',test_acc)
        return test_acc


if __name__ == '__main__':
    mnist = FashionMnist('../Fashion_mnist/')
    mnist.build()  # 组建网络
    mnist.train()
    #评估
    mnist.metrics()
    mnist.close()
