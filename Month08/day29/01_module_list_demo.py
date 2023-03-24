# 01_module_list_demo.py
# ModuleList: 操作的容器，没有强制顺序执行
import torch
from torch import nn

class Net1(nn.Module):
    def __init__(self):
        super(Net1, self).__init__()
        # 定义两个Linear层存入ModuleList
        self.linears = nn.ModuleList(
            [nn.Linear(10,10) for i in range(2)])

    def forward(self):
        for m in self.linears:
            x = m(x)
        return x

net = Net1() # 实例化模型
print(net)

# 打印模型参数
for param in net.parameters():
    print("type:", type(param.data), " size:", param.size())