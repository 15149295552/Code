# 15_variable_demo.py
# 创建变量：Variable，变量支持自动求导
import torch
from torch.autograd import Variable

a = torch.tensor([1.0, 2.0, 3.0, 4.0]) # 普通张量
print(type(a))
print(a.requires_grad) # 普通张量该属性为False
print(a)

var1 = Variable(a, requires_grad=True)
print(type(var1))
print(var1.requires_grad)
print(var1)


