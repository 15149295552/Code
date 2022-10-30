# 练习1：创建地区列表、新增列表、现有列表，至少存储3行信息。
list_city = ['香港', '云南', '广东']
list_new = [7, 2, 1]
list_now = [171, 68, 40]

# 练习2：
# 向以上三个列表追加第4行数据
list_city.append('上海')
list_new.append(2)
list_now.append(37)
print(list_city, list_new, list_now, sep='\n')

# 在第1个位置插入第5行数据
list_city.insert(0, '台湾')
list_new.insert(0, 2)
list_now.insert(0, 36)
print(list_city, list_new, list_now, sep='\n')

# 练习3：
# 打印香港疫情信息(xx地区新增xx人现存xx人)
print(f'{list_city[1]}地区新增{list_new[1]}人现存{list_now[1]}人')

# 将地区列表后2个元素修改为 ["GD","SH"]
list_city[-2:] = ["GD", "SH"]
print(list_city)

# 打印地区列表元素(一行一个)
for city in list_city:
    print(city)

# 倒序打印新增列表元素(一行一个)
for x in range(len(list_new)-1, -1, -1):
    print(list_new[x])

# 练习4：
# 在地区列表中删除“云南”
list_city.remove('云南')

# 在新增列表中删除第1个元素
del list_new[0]

# 在现有列表中删除前2个元素
del list_now[:2]
print(list_city, list_new, list_now)

# 练习5：
# 分别打印出：现有列表中最大值、最小值与总计人数。
print('最大值', max(list_now))
print('最小值', min(list_now))
print('求和', sum(list_now))