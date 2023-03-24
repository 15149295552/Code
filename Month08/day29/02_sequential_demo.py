# 02_sequential_demo.py
# Sequential示例
import torch
from torch import nn

class Net2(nn.Module):
    def __init__(self):
        super(Net2, self).__init__()
        # 定义Sequential，存入4个操作层
        self.block = nn.Sequential(nn.Conv2d(1, 20, 5),
                                   nn.ReLU(),
                                   nn.Conv2d(20, 64, 5),
                                   nn.ReLU())

    def forward(self, x):
        x = self.block(x)
        return x

net = Net2()
print(net)

for param in net.parameters():
    print("type:", type(param), " size:", param.size())