'''
练习:
    在终端中输入任意整数，计算累加和.
    "1234" -> "1" -> 累加 1

    效果：
        请输入一个整数:12345
        累加和是 15

    分析：
        1 获取任意位数的整数（str类型）
        2 遍历输入的字符串内容 --> 变量接收的是：每个字符
        3 在循环外创建变量（记录累加的和） result = 0
        4 在循环内：变量累加 int(变量)
        5 打印结果
'''

number = input('请输入一个整数：')
result = 0     # 记录累加的和

if number.isdigit():   # 判断输入的内容是否全是数字
    for x in number:
        # print(x, type(x))
        result += int(x)
    print(result)
else:
    print('输入错误')

'''
for i in number:    # int类型的数不是可迭代对象（range/容器）
    pass
for i in 'number':    # 遍历的是字符串:'number' (变量 与 字符串)
    pass
'''

