# 练习
# 根据月日,计算是这一年的第几天.
# 公式：前几个月总天数 + 当月天数
# 例如：5月10日
# 计算：31 29 31 30 + 10
tuple_day = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
month = int(input("请输入月：")) # 3
day = int(input("请输入日："))# 15
# 因为tuple_day[:2]会触发浅拷贝,
# 所以建议使用range()
# total_day = 0
# for item in tuple_day[:2]:
#     total_day += item

# total_day = 0
# for i in range(2):
#     total_day += tuple_day[i]

# 最简洁
# total_day = sum(tuple_day[:2])
total_day = sum(tuple_day[:month-1])
total_day += day
print(total_day)


