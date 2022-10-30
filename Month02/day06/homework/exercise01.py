"""
    画出下列代码内存图
"""
list01 = [10, 20, 30]
for item in list01:
    item += 1
print(list01)  # ?

list02 = [
    [10],
    [20],
    [30],
]
for item in list02:
    item[0] += 1
print(list02)  # ?
