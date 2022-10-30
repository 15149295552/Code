"""
    函数 - 引入
        做法 与 用法分离
"""
# 代码的重复就是万恶之源

# 做法(变化) + 用法
"""
print("直拳")
print("摆拳")
print("勾拳")
print("肘击")
# ...
print("直拳")
print("摆拳")
print("勾拳")
print("肘击")
"""

# 做法(变化)
def attack():
    print("直拳")
    print("摆拳")
    print("勾拳")
    print("肘击")
    print("鞭腿")

# 用法
attack()
attack()
attack()

