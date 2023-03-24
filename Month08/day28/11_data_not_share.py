# 11_data_not_share.py
# 数组、张量不共享内存
import torch
import numpy as np

arr2 = np.array([1, 2, 3, 4])
t2 = torch.from_numpy(arr2)
print(arr2)
print(t2)
print("")

arr2 = arr2 + 1 # 返回新对象，不会影响张量
print(arr2)
print(t2)
print("")

t2 = t2.add(2) # 返回新对象，不影响数组
print(arr2)
print(t2)



