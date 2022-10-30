"""
    在列表中查找最大值(不使用max,自定义算法实现)
    思路:
        假设第一个元素就是最大值
        依次与后面元素进行比较
        如果发现更大值,则替换
"""
# 重点!!
list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
max_value = list02[0]
for c in range(1, len(list02)):  # 1 2 3 4 .. 总数-1
    if max_value < list02[c]:
        max_value = list02[c]
print(max_value)

# 排序
for r in range(len(list02) - 1):  # 0        1       2
    for c in range(r + 1, len(list02)):  # 1~最后   2~最后   3~最后
        if list02[r] < list02[c]:
            list02[r], list02[c] = list02[c], list02[r]
