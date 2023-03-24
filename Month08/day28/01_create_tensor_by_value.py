# 01_create_tensor_by_value.py
# 根据传入的值创建张量
import torch
import numpy as np

a = torch.tensor(5) # 定义一个值为5的张量
print(a)

arr = np.asarray([4]) # numpy数组
a = torch.tensor(arr)
print(a)