# 14_tensor_split.py
# 张量分割
# chuck:均匀分割   split:不均匀分割
import torch

print("均匀分割示例:")
a = torch.tensor([[1, 2],
                  [2, 4],
                  [3, 6],
                  [4, 8]])
b = torch.chunk(a,
                chunks=2,  # 片段数量
                dim=0)  # 行方向进行分割
print("dim=0")
for item in b:
    print(item)
    print("")

print("dim=1")
c = torch.chunk(a, chunks=2, dim=1)  # 列分割
for item in c:
    print(item)
    print("")

print("不均匀分割示例：")
a = torch.tensor([[1, 2, 3],
                  [2, 3, 4],
                  [3, 6, 9],
                  [4, 8, 12],
                  [5, 10, 15]])
b = torch.split(a,
                split_size_or_sections=3,#每个片段大小
                dim=0)#行方向
for item in b:
    print(item)
    print("")

c = torch.split(a,
                split_size_or_sections=2,#每个片段大小
                dim=1)
for item in c:
    print(item)
    print("")
