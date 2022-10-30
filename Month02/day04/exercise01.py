"""
# 练习：累加10 -- 60之间，个位不是3/5/8的整数和。
# 思想1:不是3/5/8 则累加
# 思想2:是3/5/8 则跳过
"""
total_value = 0
for item in range(10, 61):
    # if item % 10 != 3 and item % 10 != 5 and item % 10 != 8:
    unit = item % 10
    if unit != 3 and unit != 5 and unit != 8:
        total_value += item
print(total_value)

total_value = 0
for item in range(10, 61):
    unit = item % 10
    if unit == 3 or unit == 5 or unit == 8:
        continue
    total_value += item
print(total_value)
