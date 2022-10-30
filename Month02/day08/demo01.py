"""
    函数内存分布
"""

# 1. 将代码加载到内存的"代码区"
def func01(p1, p2):
    data = p1 + p2
    return data


# 2. 调用函数时在内存中开辟一块空间(栈帧)
# 存储函数内部的变量
num01 = 10
number = func01(num01, 20)
print(number)

# 3. 函数执行后栈帧立即销毁,变量随即释放
