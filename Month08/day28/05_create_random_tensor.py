# 05_create_random_tensor.py
# 生成随机值张量
import torch

t_rand = torch.rand(10) # 均匀随机值
print(t_rand)

# 生成3行3列，均值为0标准差为1的正态随机张量
t_rand_nor = torch.randn(3, 3)
print(t_rand_nor)

t_rand_nor2 = torch.normal(mean=0.5, std=2, size=(3, 3))
print(t_rand_nor2)