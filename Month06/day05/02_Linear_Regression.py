'''
利用Python代码实现线性回归
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.5, 0.6, 0.8, 1.1, 1.4])
y = np.array([5.0, 5.5, 6.0, 6.8, 7.1])

# y = w1x + w0

# 设定模型参数初始值
w1 = 1  # 随机数,不能为0
w0 = 1  # 0 or 1
learning_rate = 0.01  # 学习率,不要设太大
epoch = 500  # 轮数

w0s,w1s,losses,epoches = [],[],[],[]
for i in range(epoch):
    # 输出每一轮更新时w0,w1,loss变化的情况
    loss = ((w1 * x + w0 - y) ** 2).sum() / 2
    print('轮数:{:3},w1:{:.8f},w0:{:.8f},loss:{:.8f}'.format(i + 1, w1, w0, loss))
    #收集模型参数及损失值,进行可视化
    w0s.append(w0)
    w1s.append(w1)
    losses.append(loss)
    epoches.append(i+1)
    # w0和w1的偏导数
    d0 = (w0 + w1 * x - y).sum()
    d1 = (x * (w0 + w1 * x - y)).sum()
    w0 = w0 - learning_rate * d0
    w1 = w1 - learning_rate * d1

# print('w0:{},w1:{}'.format(w0, w1))
# 拿到预测值
pred_y = w1 * x + w0

# 样本散点图
# plt.scatter(x, y, s=60)
# plt.plot(x, pred_y, color='orangered')
# plt.show()

#模型参数及损失值的更新情况可视化
plt.figure('LR',figsize=(10,8),facecolor='lightgray')

plt.subplot(3,1,1)
plt.plot(epoches,w1s,color='dodgerblue',label='w1')
plt.legend()
#-----
plt.subplot(3,1,2)
plt.plot(epoches,w0s,color='dodgerblue',label='w0')
plt.legend()
#-----
plt.subplot(3,1,3)
plt.plot(epoches,losses,color='orangered',label='loss')
plt.legend()

plt.show()
