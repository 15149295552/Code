# 19_no_scalar_grad.py
# 非标量求导
import torch

x = torch.tensor([1, 2], dtype=torch.float, requires_grad=True)
y = torch.tensor([2, 3], dtype=torch.float, requires_grad=True)
Q = 3 * x ** 2 - y ** 2 # 目标函数

ext_grad = torch.tensor([1.0, 1.0]) # 传入值全为1的向量
Q.backward(gradient=ext_grad)

print("x.grad:", x.grad)
print("y.grad:", y.grad)