'''
练习2：以面向对象思想,描述下列情景.
    张无忌教赵敏九阳神功
    赵敏教张无忌玉女心经

    张无忌工作挣了5000元
    赵敏工作挣了10000元

分析:
    人类:
        数据: 姓名
        方法: 教/挣钱
            教方法:
                形参: 技能名称
            挣钱方法:
                形参: 钱数
'''

class Human:
    def __init__(self, name):
        self.name = name

    def teach(self, other, skill):
        print(f'{self.name}教{other.name}{skill}')

    def work(self, money):
        print(f'{self.name}工作挣了{money}元')


zwj = Human('张无忌')
zm = Human('赵敏')
zwj.teach(zm, '九阳神功')
zm.teach(zwj, '玉女心经')

zwj.work(5000)
zm.work(10000)
