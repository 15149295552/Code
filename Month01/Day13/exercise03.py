# 练习1：遍历图形控制器

class GraphicIterator:
    '''  迭代器类 '''
    def __init__(self, data):
        self.__list_manager = data
        self.__index = -1

    def __next__(self):  # 返回下一个元素
        if self.__index == len(self.__list_manager)-1:
            raise StopIteration
        self.__index += 1
        return self.__list_manager[self.__index]

class GraphicController:
    def __init__(self):
        self.__list_graphic = []

    def add_graphic(self, name):
        self.__list_graphic.append(name)

    def __iter__(self):  # 返回一个迭代器对象
        return GraphicIterator(self.__list_graphic)

controller = GraphicController()
controller.add_graphic("圆形")
controller.add_graphic("矩形")
controller.add_graphic("三角形")

# iterator = controller.__iter__()
#
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break

for item in controller:
    print(item)