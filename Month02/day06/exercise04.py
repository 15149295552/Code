"""
# 练习2：二维列表
# --以表格状打印
# --将元素能被3整除的修改为0
"""
list01 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]
# 读取全部元素
for line in list01:
    for item in line:
        print(item,end = "\t")
    print()

for r in range(len(list01)):
    for c in range(len(list01[r])):
        if list01[r][c] % 3 == 0:
            list01[r][c] = 0
print(list01)