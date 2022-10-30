# 函数 function

# 快捷键：Ctrl + Q/Ctrl + P
# print()

# print('你好')
# print('加个微信可以吗？')
# print('有对象吗？')
#
# print('你好')
# print('加个微信可以吗？')
# print('有对象吗？')
#
# print('你好')
# print('加个微信可以吗？')
# print('有对象吗？')

# 结构1：函数无参数，无返回值
# # 定义函数
# def say_hello():
#     print('你好')
#     print('加个微信可以吗？')
#     print('有对象吗？')
#
# # 调用函数
# say_hello()
# say_hello()
# say_hello()


# 结构2：函数有参数，无返回值
# 定义函数
# def say_hello(who):    # who: 形参，用于接收函数调用传递时的实参【变量名-->抽象（'虚的'）】
#     '''
#         打招呼
#     :param who: str,打招呼的人
#     :return: None
#     '''
#     print('你好', who)
#     print('加个微信可以吗？')
#     print('有对象吗？')

# 调用函数
# say_hello('郑老师')    # 实参, 用于形参限制了需要传递的数据【实实在在的数据】
# say_hello('凤姐')
# say_hello('王心凌')

# 打印文档字符串
# print(say_hello.__doc__)

''' 结论
    1 函数不调用，不会执行
    2 调用函数执行函数内部的语句
    3 函数调用结束后，回到函数调用的位置
'''


# 结构3：函数有参数，有返回值
# def say_hello(who):    # who: 形参
#     '''
#         打招呼
#     :param who: str,打招呼的人
#     :return: None
#     '''
#     print('你好', who)
#     print('加个微信可以吗？')
#     print('有对象吗？')
#     return '没门'
#
# # 调用函数
# result = say_hello('郑老师')
# print(result)
#
# say_hello('郑老师')


# 当函数中无return语句或return语句后的数据为空，则都返回None
# def func():
#     print('这是一个函数')
#     return
#
# result = func()
# print(result)


# 函数可以返回多个数据，结果为元组类型
# def func(a, b):
#     c = a + b
#     return a, b, c
#
# result = func(2, 6)
# print(result)


# return后的语句不会执行
# def func(a, b):
#     print('这是一个函数')
#     return a + b
#     print('执行了return语句')
#
#
# result = func(2, 6)
# print(result)


# return语句在函数存在循环结构中，可以用来终止循环的执行
# def func2(number):
#     for i in range(3):
#         for i in range(number):
#             if i == 4:
#                 return
#                 # break
#             print(i, end=' ')
#
# func2(10)

'''
    return语句的作用
        1 用来返回函数执行的结果
        2 用来中断函数的执行
'''

# def func(a, b):
# 	a = 20
# 	b[0] = 20
#
# a = 10
# b = [100]
# func(a, b)
# print(a)   # 10
# print(b)   # [20]


# def func01(p1, p2):
# 	p1 = [100, 200]
# 	p2[:] = [300, 400]
#
# a = [10, 20]
# b = [30, 40]
# func01(a, b)
# print(a) # ?
# print(b) # ?



# 跨函数调用
# 需求：打印对应的年龄阶段
def age_juage(age):
	'''
		对年龄进行阶段判断并打印
	:param age: int,年龄
	:return: None
	'''
	if age <= 18:
		print('未成年人')
	else:
		print('成年人')


def print_age_result(age):
	if age > -1:
		age_juage(age)
	else:
		print('年龄值错误')

age = int(input('请输入年龄：'))
print_age_result(age)