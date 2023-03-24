# 10_data_share_demo.py
# 张量、数组数据共享示例
import torch
import numpy as np

arr = np.array([1, 2, 3, 4])
t1 = torch.from_numpy(arr)
print(arr)
print(t1)
print("")

arr += 1 # 修改数组，会影响张量
print(arr)
print(t1)
print("")

t1.add_(2) # 张量自变化计算，影响数组
print(arr)
print(t1)

