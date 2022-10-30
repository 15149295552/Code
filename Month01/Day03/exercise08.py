# 输入边长，打印数字矩形

# 边长：4
'''
    外层：行 4行（0-3） row=0 1 2 3
    内层：列 4列（range(row , side+row)）

    # 当超过2位数，从0开始（10-->0  11-->1）
'''
# side = 11
#
# for row in range(side):
#     for col in range(row, side+row):
#         print(col, end='\t')
#     print()


# 需求:当超过2位数，从0开始（10-->0  11-->1  12-->2）
# 方法1: 超过10, 对数取余, 数 % 10, 否则: 正常打印
# 方法2: 对所有的数 针对 10 取余
side = 21

for row in range(side):
    for col in range(row, side + row):
        # 方法1：
        # if col >= 10:
        #     print(col % 10, end=' ')
        # else:
        #     print(col, end=' ')

        # 方法2
        print(col % 10, end=' ')
    print()


x = 0
while x < side:
    y = x
    while y < side + x:
        print(y % 10, end=' ')
        y += 1
    x += 1
    print()               
