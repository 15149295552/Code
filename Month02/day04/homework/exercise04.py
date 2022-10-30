"""
    在终端中录入4个同学体重,打印最轻的值.
	效果：
        请输入第1个同学体重:100
        请输入第2个同学体重:120
        请输入第3个同学体重:93
        请输入第4个同学体重:160
        最轻的同学:93
"""
weight01 = float(input("请输入第1个同学体重:"))
weight02 = float(input("请输入第2个同学体重:"))
weight03 = float(input("请输入第3个同学体重:"))
weight04 = float(input("请输入第4个同学体重:"))
# 假设第一个就是最小的
min_value = weight01
# 使用假设的与后面元素比较
if min_value > weight02:
    min_value = weight02
if min_value > weight03:
    min_value = weight03
if min_value > weight04:
    min_value = weight04
print("最轻的同学：" + str(min_value))
