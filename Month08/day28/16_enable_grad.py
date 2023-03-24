# 16_enable_grad.py
# 使用enable_grad, no_grad打开和关闭梯度
import torch
from torch.autograd import Variable


# @torch.no_grad()  # 装饰器方式关闭梯度
@torch.enable_grad()  # 装饰器方式打开梯度
def doubler(x):
    return x * 2


x = torch.ones(2, 2, requires_grad=True)
print(type(x))
print(x.requires_grad)
print(x)

# with torch.no_grad():  # 关闭梯度
with torch.enable_grad():  # 打开梯度
    y = x * 2  # 张量y的梯度被关闭

print("y.requires_grad:", y.requires_grad)
print("x.requires_grad:", x.requires_grad)

z = doubler(x)  # z是函数的返回值，会受装饰器的影响
print("z.requires_grad:", z.requires_grad)
print("x.requires_grad:", x.requires_grad)
