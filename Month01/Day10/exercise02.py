# 练习2：创建店铺类，并保护数据在有效范围内
# 数据：店铺名称、店铺电话（7位、8位或11位）

'''
    保护数据: 店铺电话
    采取模式: 可读可写模式
'''

class Shop:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    @property
    def phone(self):   # 读取
        return self.__phone

    @phone.setter
    def phone(self, value):   # 写入
        if len(str(value)) in (7, 8, 11):
            self.__phone = value
        else:
            print('电话号码错误')


s01 = Shop('食客', 12345678)
print(s01.__dict__)
s02 = Shop('食客', 123456)
print(s02.__dict__)