"""
    装饰器 - 标准
"""
def new_func(func):
    def wrapper(*args,**kwargs):  # 2
        print("新功能")
        res = func(*args,**kwargs)  # 执行旧功能 # 3
        return res
    return wrapper

# old_func01 = new_func(old_func01)
@new_func
def old_func01():  # 4
    print("旧功能1")
    return 10

@new_func
def old_func02(p1, p2):  # 4
    print("旧功能2")

# 拦截:将调用旧功能改为调用内函数
# old_func01 = new_func(old_func01)
# old_func02 = new_func(old_func02)

print(old_func01())  # 1
print(old_func02(10, 20))
print(old_func02(10, p2=20))
