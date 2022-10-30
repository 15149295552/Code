# hml: house model layer  房源模型层

class HouseModel:
    def __init__(self, id=0, name=None, type='', area=10, tprice=0, uprice=0):
        self.id = id
        self.name = name
        self.type = type
        self.area = area
        self.tprice = tprice
        self.uprice = uprice

    def __str__(self):
        return f'{self.id}-{self.name}-{self.type}-{self.area}-{self.uprice}-{self.tprice}'

    @property
    def area(self):  # 读取方法
        return self.__area

    @area.setter
    def area(self, value):  # 写入方法
        if value > 10:
            self.__area = value
        else:
            raise Exception('面积至少要为10平米以上')

    @property
    def uprice(self):
        return self.__uprice

    @uprice.setter
    def uprice(self, value):
        if value > 0:
            self.__uprice = value
        else:
            raise Exception('单价必须大于0')

    @property
    def tprice(self):
        return self.__tprice

    @tprice.setter
    def tprice(self, value):  # 写入方法
        if value > 0:  # 数据校验
            self.__tprice = value
        else:
            raise Exception('总价必须大于0')
