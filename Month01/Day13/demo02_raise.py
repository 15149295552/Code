# raise语句
# 目的: 快速传递异常

# 子定义异常类
class AgeError(Exception):
    def __init__(self, code, info):
        self.code = code
        self.info = info

    def __str__(self):
        return '错误码: {}, 错误信息: {}'.format(self.code, self.info)

class Wife:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):   # 读取方法
        return self.__age

    @age.setter
    def age(self, value):  # 写入方法
        if 18 <= value <= 21:
            self.__age = value
        else:
            # 人为抛出异常
            # raise Exception('我不要')
            # 人为抛出自定义异常
            raise AgeError(1004, '年龄必须在[18, 21]之间')

try:
    w01 = Wife(19)
    print(w01.age, w01.__dict__)
    w01.age = 26
    print(w01.age)
except Exception as e:
    # print(e.code, e.info)
    print(e)