"""
    练习1：遍历商品控制器
"""
class CommodityIterator: # 迭代器
    def __init__(self,data):
        self.data = data
        self.index = -1

    def __next__(self):
        if self.index < len(self.data)-1:
            self.index += 1
            return self.data[self.index]
        raise StopIteration()

class CommodityController: #可迭代对象
    def __init__(self):
        self.list_commodity = []

    def add_commodity(self,cmd):
        self.list_commodity.append(cmd)

    def __iter__(self):
        return CommodityIterator(self.list_commodity)

controller = CommodityController()
controller.add_commodity("屠龙刀")
controller.add_commodity("倚天剑")
controller.add_commodity("芭比娃娃")
# for item in controller:
#     print(item)
iterator = controller.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
