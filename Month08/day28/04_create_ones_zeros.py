# 04_create_ones_zeros.py
# 生成值全为0或1的张量
import torch

a = torch.ones(2, 3) # 生成2行3列值全为1的张量
print(a)

b = torch.zeros(5) # 生成值全为0的张量
print(b)

c = torch.ones_like(b) # 生成和b形状相同的值全为1的张量
print(c)

