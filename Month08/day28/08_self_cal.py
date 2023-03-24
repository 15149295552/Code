# 08_self_cal.py
# 张量自变化计算
import torch

a = torch.IntTensor([2]) # 创建值为2的int型张量
print(a)

b = torch.IntTensor([3])
print(b)

a.add_(b) # 自变化计算
print(a)