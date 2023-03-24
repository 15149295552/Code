# 17_set_grad_enable_demo.py
# 统一打开或关闭梯度
import torch
from torch.autograd import Variable

# 创建一个张量
x = torch.ones(2, 2, requires_grad=True)
print(type(x))
print(x)

torch.set_grad_enabled(False) # 统一关闭梯度
y = x * 2 # 根据之前的张量计算的到的新张量
w = torch.ones(3, 3) # 重新创建一个新张量
z = torch.ones(3, 3, requires_grad=True)

print("y.requires_grad:", y.requires_grad) # 通过计算返回的张量被关闭
print("w.requires_grad:", w.requires_grad) # 创建新张量默认被关闭
print("z.requires_grad:", z.requires_grad) # 显式指定了的权限更高

torch.set_grad_enabled(True) # 统一打开梯度
m = x ** 2
print("m.requires_grad:", m.requires_grad)