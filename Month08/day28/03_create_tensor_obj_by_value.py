# 03_create_tensor_obj_by_value.py
# 根据传入的值实例化张量对象
import torch

# 以列表中的值作为初始值创建张量，类型默认为Float
a = torch.Tensor([2, 3])
print(a)

# 创建Float类型的张量, 以列表中的值作为初始值
b = torch.FloatTensor([2, 3])
print(b)

c = torch.DoubleTensor([2, 3]) # 双精度浮点型
print(c)

d = torch.IntTensor([2, 3]) # 整型
print(d)
