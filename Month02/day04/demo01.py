"""

"""
# 需求:累加1--100之间整数
# 条件:能被3整除
# 思想1:满足条件,则执行
total_value = 0
for item in range(1, 101):
    if item % 3 == 0:
        total_value += item
print(total_value)
# 思想2:不满足条件,则跳过
total_value = 0
for item in range(1, 101):  # [100个瓜子]
    if item % 3 != 0:  # [如果遇到坏的]
        continue  # 跳过(本次循环体后续代码)
        # break # 跳出(循环立即结束)
    total_value += item
print(total_value)
