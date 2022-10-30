"""
    练习3：以面向对象思想,描述下列情景.
    张无忌教赵敏九阳神功
    赵敏教张无忌玉女心经
    张无忌工作挣了5000元
    赵敏工作挣了10000元
"""


class Person:
    def __init__(self, name=""):
        self.name = name

    def teach(self,other,skill):
        print(self.name, "教", other.name,skill)

    def work(self,salary):
        print(self.name,"挣了",salary,"元")

# 用对象区分数据不同
zwj = Person("张无忌")
zm = Person("赵敏")
# teach(self, other,skill)
# teach(zwj, zm,"九阳神功")
zwj.teach(zm,"九阳神功")
# teach(zm, zwj,"玉女心经")
zm.teach(zwj,"玉女心经")
zwj.work(5000)
zm.work(10000)

"""
# 类型与类型之间行为不同
# 对象与对象之间数据不同
a1 = [10]
a2 = [20]
a1.append()
a2.append()

b = {}
b.items()
"""

