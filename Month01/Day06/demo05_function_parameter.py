# 形参的定义方式

# 缺省参数
def get_user_info(name, age=18, addr='北京市'):
    print(name, age, addr)


# get_user_info('小黑')
# get_user_info('小黑', 22)
# get_user_info('小黑', 22, '上海市')
# get_user_info('小黑', addr='上海市')


# 如果一个参数是缺省参数，其右侧的参数必须全部是缺省参数
# def func(a, b=10, c):
#     pass


# 位置形参
# 说明：形参按照位置接收实参的形式
# 注意：个数一致
def func01(a, b, c):
    print(a, b, c)

# func01(1, 3, 5)
# func01(*[1, 3, 5])
# func01(c=1, b=5, a=11)
# func01(**dict(c=1, b=5, a=11))

# 星号元组形参
# 说明：*args 表示可以接收多余【位置实参】
# def func02(a, *args):    # 【合并】多个位置实参
#     print(a, args, type(args))
#
# func02(1)
# func02(1, 4)
# func02(1, 4, 5, 6, 7, 8)
# func02(1, *[4, 5, 6, 7, 8])   # 【拆解】序列
# func02(a=1, args=55)


# 命名关键字形参
# def func03(a, *args, b):
#     print(a, args, b)

# func03(1, 3, 4)
# func03(1, 3, 4, b=9)


# * 不接收实参，限制其后面的参数在实参传递中必须使用【关键字实参】
# def func03(a, *, b):
#     print(a, b)
#
# # func03(1, 3, 4)
# func03(1, b=6)


# 双星号字典形参
# **kwargs: 用于接收多余的【关键字实参】
def func04(a, **kwargs):  # 【合并】多个关键字参数为字典
    print(a, kwargs, type(kwargs))
#
# func04(22)
func04(22, b=6)
func04(22, b=6, c=7, d=9, f=10)
func04(22, **dict(b=6, c=7, d=9, f=10))   # 【拆解】字典


# dict(**kwargs)
# print(dict(a=10, b=11, c=12))


# ‘函数的万能定义写法’
# def 函数名(*args, **kwargs):
#     pass


# 优先级
# def func(a, *args, b, **kwargs):
#     pass  # 占位（填充语法空白）

'''
    说明
        实参传递个数是否一致
            不一致
                缺省参数
                星号元组形参
                双星号字典形参
            一致
                位置形参
                命名关键字形参
        
        形参个数不一定
            不定长
                星号元组形参：多个位置实参
                双星号字典形参：多个关键字实参
                
            定长
                位置形参
                命名关键字形参
            
    优先级
        位置形参 > 星号元组形参 > 命名关键字形参 > 双星号字典形参
'''