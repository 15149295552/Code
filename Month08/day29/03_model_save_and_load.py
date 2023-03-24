# 03_model_save_and_load.py
# 模型保存与加载：同时保存模型、参数
import torch
import torch.nn as nn
import torch.optim as optim

# 定义模型
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(1, 2)
        self.fc2 = nn.Linear(2, 1)

    def forward(self, x):
        x = torch.sigmoid(self.fc1(x))
        x = self.fc2(x)
        return x

# 定义样本
x = torch.linspace(0, 1, 10).reshape(10, 1) # 生成10个样本
y = x * x - 0.5 * x - 1.5625 # y

net = Net() # 实例化模型对象
optimizer = optim.SGD(net.parameters(), lr=0.1)# 优化器

for n in range(0, 10000):
    optimizer.zero_grad() # 梯度清除
    y_pred = net(x) # 前向计算
    loss = sum((y_pred - y) ** 2) / 2 # 均方差

    loss.backward() # 反向传播
    optimizer.step() # 更新参数

    if n % 1000 == 0:
        print(n, loss)
print("训练结束.")

# 保存模型
torch.save(net, "model/mynet.pt")
print("保存模型成功.")

# 加载模型
net2 = torch.load("model/mynet.pt")
test_y = [] # 预测结果
test_x = torch.linspace(0, 1, 100).reshape(100, 1)#生成100个测试样本
for sample in test_x:
    y_hat = net2(sample) # 执行预测
    test_y.append(torch.detach(y_hat).numpy()[0])

# 绘图
import matplotlib.pyplot as plt
plt.plot(x, y, "k*") # 训练样本
plt.plot(torch.detach(test_x).numpy(), test_y, "b-") # 新模型预测线
plt.show()

