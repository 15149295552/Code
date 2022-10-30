# 练习1：遍历图形控制器

class GraphicController:
    def __init__(self):
        self.__list_graphic = []

    @property
    def list_praphic(self):
        return self.__list_graphic

    def add_graphic(self, name):
        self.__list_graphic.append(name)

def get_graphic(lists):
    index = 0
    while index < len(lists):
        yield lists[index]
        index += 1

controller = GraphicController()
controller.add_graphic("圆形")
controller.add_graphic("矩形")
controller.add_graphic("三角形")
list_graphic = controller.list_praphic

# iterator = controller.__iter__()
#
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break

for item in get_graphic(list_graphic):
    print(item)