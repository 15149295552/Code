# 09_numpy_to_tensor.py
# numpy对象转换为张量
import torch
import numpy as np

arr = np.array([[1, 2, 3], [ 4, 5, 6]])
print(type(arr))
print(arr)
print("---------------")

# from_numpy方法转换
t1 = torch.from_numpy(arr)
print(type(t1))
print(t1)
print("---------------")

# 创建张量的方式
t2 = torch.tensor(arr)
print(type(t2))
print(t2)
print("---------------")

t3 = torch.Tensor(arr)
print(type(t3))
print(t3)
print("---------------")

# 张量转数组：tensor.numpy()
arr1 = t3.numpy()
print(type(arr1))
print(arr1)