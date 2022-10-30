# # 集合 set
#
# # 表示
# # {元素1, 元素2, ...}
#
# # 创建
# # 1 空集合
# s01 = set()
# print(s01, type(s01))
#
# # 2 存储无序，且元素是不可变数据类型
# s02 = {2, 3.4, False, 'java', (1, 3)}
# print(s02)
# # s02 = {[3, 5]}   # TypeError: unhashable type: 'list'
# # print(s02)
#
# # 3 构造函数：set(可迭代对象)  --> 价值1：去重
# s03 = set(range(5))
# s03 = set('java')   # 不重复
# print(s03)
#
# # 查看
# print('长度:', len(s03))
# print('存在:', 5 not in s03)
#
# # 增加
# s04 = {'v', 'j', 'a'}
# s04.add('C')
# print(s04)
#
# # 删除
# s04.remove('C')
# # s04.remove('A')   # KeyError: 'A'
# print(s04)
# s04.discard('A')
# print(s04)
#
# # 遍历
# for s in s04:
#     print(s)


# 价值2：运算
# s01 = {1, 3, 4, 5}
# s02 = {2, 3, 5, 6}
# s03 = {1, 2, 3, 4, 5, 6}
#
# print('交集：', s01 & s02)
# print('并集：', s01 | s02)
# print('补集：', s01 - s02)
# print('补集：', s02 - s01)
# print('对称集：', s02 ^ s01)
# print('子集：', s02 < s01)   # 包含
# print('子集：', s02 < s03)   # 包含
# print('超集：', s02 > s03)   # 包含
# print('超集：', s03 > s01)   # 包含


# 集合推导式
# 将1-10之间的所有数的平方存储到集合中
# 常规方法
set01 = set()
for i in range(1,10):
    set01.add(i**2)
print(set01)

# 推导式
print({i**2 for i in range(1,10)})
print({i**2 for i in range(1,10) if i % 2 == 0})

