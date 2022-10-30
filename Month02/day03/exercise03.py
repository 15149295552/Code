"""
    练习3：
    在终端中录入4个同学身高,打印最高的值.
"""
height01 = int(input("请输入身高:"))
height02 = int(input("请输入身高:"))
height03 = int(input("请输入身高:"))
height04 = int(input("请输入身高:"))
max_value = height01
if max_value < height02:
    max_value = height02
if max_value < height03:
    max_value = height03
if max_value < height04:
    max_value = height04
print("最大值:" + str(max_value))
