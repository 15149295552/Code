# 13_tensor_cat.py
# 张量连接
import torch
import numpy as np

t1 = torch.tensor([[1, 2], [3, 4]])
t2 = torch.tensor([[5, 6], [7, 8]])
print(t1)
print(t2)
print("")

# cat:张量连接   dim参数设置连接的维度
t3 = torch.cat([t1, t2], dim=0) # 纵向连接
print(t3)

t4 = torch.cat([t1, t2], dim=1) # 横向连接
print(t4)

#################################

tt_1 = torch.tensor([[[1, 1],
                      [2, 2]],
                     [[3, 3],
                      [4, 4]],
                     [[5, 5],
                      [6, 6]]]) # (3, 2, 2)
tt_2 = torch.tensor([[[11, 11],
                      [22, 22]],
                     [[33, 33],
                      [44, 44]],
                     [[55, 55],
                      [66, 66]]])# (3, 2, 2)
tt_3 = torch.cat([tt_1, tt_2], dim=0) # 0:深度方向叠加
# tt_3 = torch.cat([tt_1, tt_2], dim=1) # 1:行叠加
# tt_3 = torch.cat([tt_1, tt_2], dim=2) # 2:列叠加
print(tt_3.shape)
print(tt_3)






