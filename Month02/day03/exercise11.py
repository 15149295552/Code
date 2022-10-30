"""
# 练习:
# 在终端中输入任意整数，计算累加和.
# "1234" -> "1" -> 累加 1
# 效果：
# 请输入一个整数:12345
# 累加和是 15
"""
number = input("请输入数字：")
total_number = 0
for item in number: # "1234"
    total_number += int(item)
print(total_number)


