# 12_reshape_demo.py
# 张量变维
import numpy as np
import torch

t1 = torch.tensor(([[1, 2],
                    [3, 4],
                    [5, 6]])) # 3行2列
print(t1.shape)
print(t1)
print("")

t2 = torch.reshape(t1, (1, 6)) # 变成1行6列
print(t2.shape)
print(t2)
print("")

t3 = torch.reshape(t1, (-1, 3)) # 列数为3，行数根据计算确定
print(t3.shape)
print(t3)
print("")
