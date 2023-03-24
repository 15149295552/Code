# 06_is_tensor.py
# 判断对象是否为张量
import torch
import numpy as np

a = torch.Tensor(2)
print(torch.is_tensor(a)) # True

b = np.array([1, 2, 3, 4])
print(torch.is_tensor(b)) # False