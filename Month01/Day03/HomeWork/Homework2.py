'''
作业2：
    在终端中录入4个同学身高,打印最高的值.

    效果：
        请输入第1个同学身高:170
        请输入第2个同学身高:160
        请输入第3个同学身高:180
        请输入第4个同学身高:165
        最高的同学:180

    分析：
        假设法
            1 假设第一个同学的身高最高
            2 依次与后面的同学的身高进行比较
            3 需要使用变量 max_height 记录最高的身高值
'''

height1 = int(input('请输入第1个同学身高: '))
height2 = int(input('请输入第2个同学身高: '))
height3 = int(input('请输入第3个同学身高: '))
height4 = int(input('请输入第4个同学身高: '))

max_height = height1

if max_height < height2:
    max_height = height2

if max_height < height3:
    max_height = height3

if max_height < height4:
    max_height = height4

print('最高的身高是：', max_height)


# 方法2
i = 0
max_height = 0

while i < 4:
    height = int(input('输入身高'))
    if height > max_height:
        max_height = height
    i += 1
print(max_height)
