"""
    练习:对数字列表进行降序排列（大 --> 小）
"""
list01 = [5, 5, 65, 65, 76, 7, 87, 89]
for r in range(len(list01) - 1):
    for c in range(r + 1, len(list01)):
        if list01[r] < list01[c]:
            list01[r], list01[c] = list01[c], list01[r]
print(list01)
