# 20_lr.py
# 自定义模型实现线性回归
import torch
from matplotlib import pyplot as plt
from torch.autograd import Variable
from torch import nn

# 自定义模型
class LinearRegression(nn.Module):
    def __init__(self):
        super(LinearRegression, self).__init__()
        # 定义操作，将需要的操作存放到对象属性中
        self.linear = nn.Linear(1, 1)

    def forward(self, x): # 重新forward方法
        out = self.linear(x)
        return out

# 定义一个模型示例
model = LinearRegression()
print(model)

epochs = 1000 # 迭代轮次
learning_rate = 1e-2 # 学习率
Loss = torch.nn.MSELoss() # 损失函数对象
optimizer = torch.optim.SGD(model.parameters(),#指定优化的参数
                            lr=learning_rate) # 学习率

# 定义样本
# unsqueeze: 插入一个维度
x = Variable(torch.unsqueeze(torch.linspace(-1, 1, 40), dim=1))
y = Variable(x * 2 + 5 + torch.rand(x.size())) # y=2x+5,并添加随机噪声

loss_list = [] # 记录损失值
epoch_list = [] # 记录迭代轮次

for epoch in range(epochs):
    y_pred = model(x) # 做前向计算(根据输入计算输出，会调用forward函数)
    loss = Loss(y_pred, y) # 计算loss
    optimizer.zero_grad() # 清空梯度

    loss.backward() # 反向传播
    optimizer.step() # 更新参数

    loss_list.append(torch.detach(loss).numpy()) # detach去掉自动微分功能
    epoch_list.append(epoch)
    if epoch % 100 == 0:
        print("[%d / %d] loss:%.5f" % (epoch, epochs, loss))

# 可视化
plt.figure("Linear Regression")
plt.title("Linear Regression")
plt.scatter(x.data.numpy(), y.data.numpy()) # 样本散点图
plt.plot(x.data.numpy(), y_pred.data.numpy(), "r-") # 回归出的模型直线

plt.figure("Loss")
plt.title("Loss")
plt.plot(epoch_list, loss_list, c="red")

plt.show()