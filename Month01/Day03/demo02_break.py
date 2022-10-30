# break语句使用

# - (1) while/for循环中执行了break语句，则后面的代码不再执行。
# - (2) while/for循环中执行了break语句，则else部分不执行。
# - (3) 只能用在循环中(while/for)。

# for i in range(1, 10):
#     if i == 4:
#         break    # 结束当前循环
#     print(i, end=' ')
# else:   # 当可迭代对象种无数据执行
#     print('for循环结束')

# i = 4
# if i == 4:
#     break


# 使用场景： while 死循环
# 题目：输入为空，则结束输入
while True:
    data = input('请输入：')
    if data == '':
    # if not data:    # if not bool(''):
        break