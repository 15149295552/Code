# 生成器 generator

# class SkillIterator:
#     '''  技能迭代器类  '''
#     def __init__(self, skill_data):
#         self.__skills = skill_data
#         self.__skill_index = -1
#
#     def __next__(self):   # 获取下[一个]技能数据
#         # 当索引值与列表的长度减一相等时,则表示迭代器中无数据,
#         if self.__skill_index == len(self.__skills)-1:
#             raise StopIteration
#         self.__skill_index += 1
#         return self.__skills[self.__skill_index]


# class Skill:
#     def __init__(self):
#         self.__list_skill = []
#
#     @property
#     def list_skill(self):  # 技能列表的读取方法
#         return self.__list_skill
#
#     def add_skill(self, name):
#         self.__list_skill.append(name)
#
#     def __iter__(self):
#         print('准备开始返回数据...')
#         print('开始返回第1个数据')
#         yield self.__list_skill[0]
#         print('开始返回第2个数据')
#         yield self.__list_skill[1]
#         print('开始返回第3个数据')
#         yield self.__list_skill[2]
#         print('数据返回完毕...')
#
# skill = Skill()
# skill.add_skill('九阴白骨爪')
# skill.add_skill('大威天龙')
# skill.add_skill('一指禅')
#
# # 1 调用__iter__方法,返回生成器对象
# generator = skill.__iter__()
# print(generator, type(generator))
#
# while True:
#     try:
#         # 2 通过迭代器调用__next__方法,获取一个数据
#         item = generator.__next__()
#         print(item)
#     # 3 当迭代器中无数据,则触发 StopIteration 异常
#     except StopIteration:
#         break


# # 生成器函数：含有 yield 语句的函数
# def get_skill(list_skill):
#     index = 0
#     while index < len(list_skill):
#         yield list_skill[index]
#         index += 1
#
# list_skill = ['九阴白骨爪', '大威天龙', '一指禅']
#
# res = get_skill(list_skill)
# print(res, type(res))   # generator object： 生成器 = 迭代器 + 可迭代对象


# # 1 调用__iter__方法,返回生成器对象
# generator = res.__iter__()
# print(generator, type(generator))
#
# while True:
#     try:
#         # 2 通过迭代器调用__next__方法,获取一个数据
#         item = generator.__next__()
#         print(item)
#     # 3 当迭代器中无数据,则触发 StopIteration 异常
#     except StopIteration:
#         break


# 生成器函数：含有 yield 语句的函数
def get_skill(list_skill):
    index = 0
    while index < len(list_skill):
        yield list_skill[index]
        index += 1

list_skill = ['九阴白骨爪', '大威天龙', '一指禅']

# res = get_skill(list_skill)
# print(res, type(res))

for data in get_skill(list_skill):
    print(data)