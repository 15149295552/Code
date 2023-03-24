# 07_type_change.py
# 张量类型转换
import torch

t_float = torch.FloatTensor([1, 2, 3])# 先创建浮点型张量
print(t_float)

# type函数转换
t_int = t_float.type(torch.IntTensor) # 括号中的参数为目标类型
print(t_int)

t_int2 = t_float.int() # 转换为整型
print(t_int2)

t_double = t_int.double() # 转换为double类型
print(t_double)