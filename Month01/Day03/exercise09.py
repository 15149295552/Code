'''
在终端中获取一个整数，作为边长，打印矩形。

效果：
请输入整数:5
$$$$$  0  '$' * side
$   $     '$' + ' ' * (side - 2) + '$'
$   $
$   $
$$$$$  4 = side - 1
'''

side = int(input('请输入边长：'))

if side > 0:
    for i in range(side):
        if i == 0 or i == side - 1:
            print('$' * side)
        else:
            print('$' + ' ' * (side - 2) + '$')
else:
    print('边长输入错误')

