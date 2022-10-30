# 列表 list

# 创建
# 1 空列表
# list01 = []   # 推荐
# list01 = list()
# print(list01, type(list01))

# 2 存储任意类型元素
# list02 = [3, 4.2, True, None, 'python', [1, 3]]
# print(list02)

# 3 构造函数：list(可迭代对象)
# print(list(range(5)))
# print(list('java'))

# 增加
# list02 = ['张飞', '刘洋', '刘赫', '全杰']
# # 追加（列表是有序）
# list02.append('杨宁')
# print(list02)
# # 插入
# list02.insert(1, '郑德')
# print(list02)
# # 追加多个元素
# list02.extend(['武鑫', '李鑫'])
# print(list02)

# 定位
# list03 = ['张飞', '刘洋', '刘赫', '全杰']
# print('长度：', len(list03))
# print('存在：', '飞' in list03)   # 判断【元素】是否在列表中
# print('索引:', list03[1])
# # print('索引:', list03[5])    # 注意：索引值越界
# print('切片:', list03[:])
# print('切片:', list03[:3])
# print('切片:', list03[-3:])

# 修改（列表是【可变】）
# list04 = ['张飞', '刘洋', '刘赫', '全杰']
# # 修改单个元素
# list04[1] = '张智'    # 修改列表中变量所关联的数据对象
# print(list04)
#
# # 修改多个元素
# list04[:2] = ['杨红瑞']   # 切片元素个数：2，数据的个数：1
# print(list04)    # ['杨红瑞', '刘赫', '全杰']
# list04[:2] = ['杨红瑞', '白永', '马鹏']   # 切片元素个数：2，数据的个数：3
# print(list04)    # ['杨红瑞', '白永', '马鹏', '全杰']
# list04[:2] = ['白永', '马鹏']   # 切片元素个数：2，数据的个数：2
# print(list04)    # ['白永', '马鹏', '马鹏', '全杰']
# # list04[::2] = ['杨红瑞', '白永', '马鹏']    # 切片元素个数：2，数据的个数：3
# # print(list04)
# # list04[::2] = ['杨红瑞']    # 切片元素个数：2，数据的个数：1
# # print(list04)
# list04[::2] = ['杨红瑞', '白永']    # 切片元素个数：2，数据的个数：1
# print(list04)

# 注意：切片赋值，当步长不为1时，切片元素个数必须等于数据元素个数


# 删除
# list05 = ['张飞', '刘洋', '刘赫', '全杰', '刘洋']

# 从左往右，删除第一匹配的元素
# list05.remove('刘洋')
# list05.remove('刘洋')
# print(list05)

# 删除索引值对应的元素
# del list05[-1]
# print(list05)

# 清空列表
# list05.clear()
# print(list05)


# 遍历
# list05 = ['张飞', '刘洋', '刘赫', '全杰']

# 将列表中的所有元素依次打印
# for item in list05:
#     print('姓名为：', item)

# 将列表中的所有元素及排名依次打印
# for i in range(len(list05)):
#     print(f'姓名为：{list05[i]},排名：{i+1}')

# 将列表中的所有元素及排名反向依次打印
# for i in range(len(list05)-1, -1, -1):   # range(3, -1, -1) --> 3 2 1 0
#     print(f'姓名为：{list05[i]},排名：{i+1}')


# 排序
# list06 = ['张飞', '刘洋', '刘赫', '全杰']
# list06.sort()
# print(list06)
# list06 = [-4, 11, 3, 99, 8]
# list06.sort()   # 默认升序
# print(list06)
# list06.sort(reverse=True)   # 降序
# print(list06)


# 二维列表的操作
# list07 = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
#
# print('索引:', list07[1][1])
#
# # 遍历所有元素（循环嵌套）
# for line in list07:   # 遍历每个小列表
#     for item in line:  # 遍历每个小列表中的元素
#         print(item)


# 浅拷贝
# # 1层列表：完全复制
# list01 = [1, 2, 3]
# list02 = list01[:]
# list03 = list01.copy()
#
# print(list01, list02, list03)
# print(id(list01), id(list02), id(list03))
#
# list01[1] = 'two'
# print(list01, list02, list03)


# 2层列表：第2层或更多层都是使用的同一个列表
# list01 = [1, 2, [3, 4]]
# list02 = list01[:]
# list03 = list01.copy()
#
# print(list01, list02, list03)
# print(id(list01), id(list02), id(list03))
#
# list01[-1][0] = 'three'
# print(list01, list02, list03)
# print(id(list01[-1]), id(list02[-1]), id(list03[-1]))


# 深拷贝
# # 1层列表：完全复制
# from copy import deepcopy
#
# list01 = [1, 2, 3]
# list02 = deepcopy(list01)
# print(list01, list02)
# print(id(list01), id(list02))
# list01[1] = 'two'
# print(list01, list02)


# 2层列表：完全复制
# from copy import deepcopy
#
# list01 = [1, 2, [3, 4]]
# list02 = deepcopy(list01)
# print(list01, list02)
# print(id(list01), id(list02))
#
# list01[-1][1] = 'four'
# print(list01, list02)
# print(id(list01[-1]), id(list02[-1]))


# 列表与字符串的互操作
# 字符串 --> 列表
data = '3室1厅 | 朝南 | 毛坯房'
# result = data.split(' | ')     # 按“ | ” 分割
result = data.split(' | ', 1)    # 按“ | ” 分割1次
print(result)

data = 'a b  c   d     e'
print(data.split())   # 默认按照任意个空格分割

# 列表 --> 字符串
lists = ['北京市', '东城区', '天坛中心']
print(''.join(lists))
print('-'.join(lists))