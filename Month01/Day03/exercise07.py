# 数字坐标矩阵
# (行号, 列号)
# 循环嵌套：
#   外层循环：行（慢） --> 0 - 3
#   内层循环：列（快） --> 0 - 3

for i in range(4):
    for j in range(4):
        print((i, j), end=' ')
    print()

x = 0
while x < 4:
    y = 0
    while y < 4:
        print((x, y), end=' ')
        y += 1
    print()
    x += 1

''' 外层执行1次，内层循环执行1圈  （外层：分针  内层：秒针）'''