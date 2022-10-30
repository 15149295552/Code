"""
    函数参数
        实际参数
            位置实参:按照顺序进行对应
            关键字实参:按照名字进行对应
"""

# 位置形参:实参必须提供
def func01(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)

# 默认形参:实参不提供时使用默认值
def func02(p1=0, p2="", p3=True):
    print(p1)
    print(p2)
    print(p3)

# TypeError: func01() missing 1 required positional argument: 'p3'
# 缺少1个位置实参
# func01(1,2)

# TypeError: func01() takes 3 positional arguments but 4 were given
# 需要3个位置实参,但是给了4个
# func01(1,2,3,4)
func01(1, 2, 3)
func02()
func02(p2="pp")
func02(p3=False)
func02(p2="pp", p3=False)
func02(10, p3 = False)