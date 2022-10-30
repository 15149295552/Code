"""
    自定义餐厅列表持久化存储
        创建餐厅类、餐厅列表
        向文件写入
        从文件读取
"""
class RestaurantModel:
    def __init__(self, city="", name="", remark=0, money=0, rid=0):
        self.city = city
        self.name = name
        self.remark = remark
        self.money = money
        self.rid = rid

    def __repr__(self):
        return f'RestaurantModel("{self.city}","{self.name}",{self.remark},{self.money},{self.rid})'

list_restaurant = [
    RestaurantModel("北京","全聚德",1000,300,1001),
    RestaurantModel("上海","城隍庙",2000,60,1002),
]

with open("b.txt","w",encoding="utf-8") as file_object:
    line = list_restaurant.__repr__()
    file_object.write(line)

with open("b.txt","r",encoding="utf-8") as file_object:
    line = file_object.read()
    new = eval(line)
    print(new[0])
    print(new[1])