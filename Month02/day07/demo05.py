"""
    返回值 各种语法
"""
def func01():
    print("func01执行了")
    return 100 # 发送

def func02():
    print("func02执行了")
    # 2. Python语言默认返回None

def func03():
    print("func03执行了")
    return 10 # 3. return 可以退出函数
    return 20
    return 30

# 接收
number = func01()
# 1. 调用者也可以不接收返回值
func01()
data = func02()
print(data)
print(func03())