'''
    分别使用while循环或for循环实现以下结果的打印
    1  2  3  4  5
    6  7  8  9  10
    11 12 13 14 15
    16 17 18 19 20

    分析：
        1 循环生产1-20的整数（不换行）
        2 考虑：换行的问题
            规律：如果数是5的倍数，则换行
                if number % 5 == 0:
                    '\n' --> 打印：print() --> 利用 print函数的参数： end默认 '\n'
        3 考虑：if 语句添加的问题
            if 语句放在 打印之后
'''
for i in range(1, 21):
    print(i, end='\t')    # '\t' 水平制表符（动态产生空格）
    if i % 5 == 0:
        print()    # 换行

x = 1
while x < 21:
    print(x, end='\t')
    if x % 5 == 0:
        print()
    x += 1

'''
    while循环
        初始条件      循环条件      变化条件
        x=1          x < 21       x += 1
    
    for 循环（range函数）
        起始值        终止值        步长
        start=1      stop=21      step=1
'''