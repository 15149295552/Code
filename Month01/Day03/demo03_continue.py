# continue语句

# - (1) while循环中执行了continue语句，后面的代码不再执行。
# - (2)  只能用在循环中(while/for)。

# 需求：打印1-20之间的个位不是3的数
# for i in range(1,20):
#     # 方法1：
#     # if i % 10 != 3:
#     #     print(i, end=' ')
#
#     # 方法2：
#     if i % 10 == 3:
#         continue   # 跳过本次循环，继续一次新的循环
#     print(i, end=' ')


# 需求：逢7过（个位是7或7的倍数，则跳过）
# 注意：在while循环中，一定要将变化条件放置在continue语句之前，否则会产生死循环
i = 0
while i < 30:
    i += 1
    if i % 10 == 7 or i % 7 == 0:
        continue
    print(i, end=' ')
