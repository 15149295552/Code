# 02_create_tensor_by_shape.py
# 根据指定的形状创建张量
import torch

ts_1 = torch.Tensor(5) # 括号中的值为形状
print(ts_1)

ts_2 = torch.Tensor(2, 3) # 创建2行3列的张量
print(ts_2)

ts_3 = torch.Tensor(2, 3, 4) # 创建2个3行4列的张量
print(ts_3)