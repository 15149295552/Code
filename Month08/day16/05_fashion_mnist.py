'''
服饰识别
使用自定义卷积神经网络实现服饰识别
'''
import tensorflow as tf
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets


class FashionMnist:
    out_feature1 = 12  # 第一组卷积核数量
    out_feature2 = 24  # 第二组卷积核数量
    con_neurons = 512  # 全连接层神经元数量

    def __init__(self, path):
        self.data = read_data_sets(path, one_hot=True)
        self.sess = tf.Session()

    def close(self):
        self.sess.close()

    def init_weight_var(self, shape):
        # 初始化权重变量
        init_val = tf.truncated_normal(shape, stddev=0.1)
        return tf.Variable(init_val)

    def init_bias_var(self, shape):
        init_val = tf.constant(1.0, shape=shape)
        return tf.Variable(init_val)

    def conv2d(self, x, w):
        # 二维卷积
        return tf.nn.conv2d(x,  # 输入数据
                            w,  # 卷积核
                            strides=[1, 1, 1, 1],  # 样本数量，高度，宽度，通道数
                            padding='SAME')  # 同维卷积

    def max_pool_2x2(self, x):
        '''2*2区域最大池化'''
        return tf.nn.max_pool(x,
                              ksize=[1, 2, 2, 1],
                              strides=[1, 2, 2, 1],
                              padding='SAME')

    def create_conv_pool_layer(self, input, input_feature, out_feature):
        '''
        卷积池化组
        :param input: 输入数据
        :param out_feature: 输出通道数量
        :param input_feature: 输入通道数量
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
        :param h_pool_flat: 输入数据（卷积池化组拉伸成一维的特征）
        :param input_feature: 输入特征数量
        :param con_neurons: 神经元数量
        :return:
        '''
        w_fc = self.init_weight_var([input_feature, con_neurons])
        b_fc = self.init_bias_var([con_neurons])
        h_fc = tf.nn.relu(tf.matmul(h_pool_flat, w_fc) + b_fc)
        return h_fc

    def build(self):
        # 组建CNN
        # 占位符
        self.x = tf.placeholder('float32', shape=[None, 784])
        x_image = tf.reshape(self.x, [-1, 28, 28, 1])
        self.y = tf.placeholder('float32', shape=[None, 10])
        # 搭建网络
        # 第一组卷积池化
        h_pool1 = self.create_conv_pool_layer(x_image, 1, self.out_feature1)
        # 第二组卷积池化
        h_pool2 = self.create_conv_pool_layer(h_pool1,
                                              self.out_feature1,
                                              self.out_feature2)
        # 全连接
        h_pool2_flat_features = 7 * 7 * self.out_feature2
        h_pool2_flat = tf.reshape(h_pool2, shape=[-1, h_pool2_flat_features])
        h_fc = self.create_fc_layer(h_pool2_flat,
                                    h_pool2_flat_features,
                                    self.con_neurons)
        # 丢弃层
        drop = tf.nn.dropout(h_fc, keep_prob=0.5)
        # 输出层
        w_fc = self.init_weight_var([self.con_neurons, 10])
        b_fc = self.init_bias_var([10])
        pred_y = tf.matmul(drop, w_fc) + b_fc
        # 损失函数
        cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits=pred_y,  # 预测值
                                                                labels=self.y)  # 真实值
        avg_cost = tf.reduce_mean(cross_entropy)
        # 梯度下降
        self.train_op = tf.train.AdamOptimizer(0.001).minimize(avg_cost)
        # 准确率
        corr = tf.equal(tf.argmax(self.y, 1),
                        tf.argmax(pred_y, 1))
        self.accuracy = tf.reduce_mean(tf.cast(corr, 'float32'))

    def train(self):
        # 初始化
        self.sess.run(tf.global_variables_initializer())
        batch_size = 100
        print('开始训练.......')

        for i in range(2):
            total_batch = int(self.data.train.num_examples / batch_size)
            total_acc = 0.0
            for j in range(total_batch):
                # 拿到一个批次数据
                train_x, train_y = self.data.train.next_batch(batch_size)
                t, acc = self.sess.run([self.train_op, self.accuracy],
                                       feed_dict={self.x: train_x, self.y: train_y})
                total_acc += acc
            avg_acc = total_acc / total_batch
            print('轮数:{},准确率:{}'.format(i + 1, avg_acc))

    def metrics(self):
        test_x, test_y = self.data.test.next_batch(10000)
        params = {self.x: test_x, self.y: test_y}
        acc = self.sess.run(self.accuracy,
                            feed_dict=params)
        print('TestAcc:',acc)


if __name__ == '__main__':
    mnist = FashionMnist('../fashion_mnist/')
    mnist.build()
    mnist.train()
    mnist.metrics()
    mnist.close()
