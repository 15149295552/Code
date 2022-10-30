"""
    列表练习
"""
# 练习1：创建地区列表、新增列表、现有列表，累计列表分别存储3行(台湾、山西、浙江)信息
list_region = ["台湾", "陕西", "浙江"]
list_new = [16, 182, 2]
list_now = [2339, 859, 505]
list_total = [16931, 1573, 2008]
# 练习2：
# 向以上四个列表追加数据第4行(广西)信息
# 在第1个位置插入第5行(香港)信息
list_region.append("广西")
list_new.append(6)
list_now.append(256)
list_total.append(599)

list_region.insert(0, "香港")
list_new.insert(0, 9)
list_now.insert(0, 196)
list_total.insert(0, 12598)
# 练习3：
# 在地区列表读取前两个元素
# 在新增列表读取后三个元素
# 将现有列表所有元素设置为0
# 打印台湾疫情信息(xx地区新增xx人现有xx人)
print(list_region[:2])
print(list_new[-3:])
list_now[:] = [0] * len(list_new)
print(list_region)
print("%s地区新增%s人现有%s人" % (list_region[1], list_new[1], list_now[1]))

# 练习4：
# 在地区列表中删除“浙江”
if "浙江" in list_region:
    list_region.remove("浙江")
# 在新增列表中删除第1个元素
del list_new[0]
# 在现有列表中删除前2个元素
del list_now[:2]
# 在累计列表中删除全部元素
del list_total[:]

# 练习5：
# 打印地区列表元素(一行一个)
for item in list_region:
    print(item)
# 新增列表元素累加2
for i in range(len(list_new)):
    list_new[i] += 2
# 打印现有列表小于1000的元素
for item in list_now:
    if item < 1000:
        print(item)
# 累计列表小于2000的元素设置为0
for i in range(len(list_total)):
    if list_total[i] < 2000:
        list_total[i] = 0