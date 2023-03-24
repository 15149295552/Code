# 18_scalar_grad.py
# 标量自动微分示例
import torch

x = torch.Tensor([2])
# 定义w,b
w = torch.randn(1, requires_grad=True)
b = torch.randn(1, requires_grad=True)
# 前向传播计算
y = torch.mul(w, x) # wx
z = torch.add(y, b) # y+b

# 打印张量的is_lear属性
print("x.is_leaf:", x.is_leaf)
print("w.is_leaf:", w.is_leaf)
print("b.is_leaf:", b.is_leaf)
print("y.is_leaf:", y.is_leaf)
print("z.is_leaf:", z.is_leaf)
# 打印非叶子节点的grad_fn函数
print("y.grad_fn:", y.grad_fn)
print("z.grad_fn:", z.grad_fn)
print("x.grad_fn:", x.grad_fn)

print("反向传播:")
z.backward() # 反向传播求梯度

print("w.grad:", w.grad)
print("b.grad:", b.grad)
print("y.grad:", y.grad)
print("z.grad:", z.grad)

