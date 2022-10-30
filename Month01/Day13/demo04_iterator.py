# 迭代器 iterator

# 需求: 定义技能类,用于添加技能和获取技能

class SkillIterator:
    '''  技能迭代器类  '''
    def __init__(self, skill_data):
        self.__skills = skill_data
        self.__skill_index = -1

    def __next__(self):   # 获取下[一个]技能数据
        # 当索引值与列表的长度减一相等时,则表示迭代器中无数据,
        if self.__skill_index == len(self.__skills)-1:
            raise StopIteration
        self.__skill_index += 1
        return self.__skills[self.__skill_index]


class Skill:
    def __init__(self):
        self.__list_skill = []

    @property
    def list_skill(self):  # 技能列表的读取方法
        return self.__list_skill

    def add_skill(self, name):
        self.__list_skill.append(name)

    def __iter__(self):
        # 返回迭代器对象
        return SkillIterator(self.__list_skill)

skill = Skill()
skill.add_skill('九阴白骨爪')
skill.add_skill('大威天龙')
skill.add_skill('一指禅')

# 1 调用__iter__方法,返回迭代器对象
iterator = skill.__iter__()

while True:
    try:
        # 2 通过迭代器调用__next__方法,获取一个数据
        item = iterator.__next__()
        print(item)
    # 3 当迭代器中无数据,则触发 StopIteration 异常
    except StopIteration:
        break