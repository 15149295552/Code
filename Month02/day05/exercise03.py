"""
    画出下列代码内存图
"""
list01 = [1, 9, 8, 6, 0, 8, 6, 3, 3, 4]
for item in list01:
    if item < 5:
        print(item)

for i in range(len(list01)):
    if list01[i] < 5:
        list01[i] = 5