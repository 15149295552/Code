# 名片模型模块

class CardModel:
    def __init__(self, name='', com_name='', phone=0, job='', id=0):
        self.id = id  # ID
        self.name = name  # 姓名
        self.com_name = com_name  # 公司名
        self.phone = phone  # 电话
        self.job = job  # 职位

    @property
    def phone(self):   # 电话读取方法
        return self.__phone

    @phone.setter
    def phone(self, value):   # 电话写入方法
        if len(str(value)) in (7, 8, 11):
            self.__phone = value
        else:
            raise Exception('电话错误')
