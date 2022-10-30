# # 静态方法 staticmethod
#
# # 需求: 获取某个方向指定个数的坐标位置
# class Location:
#     def __init__(self, row, col):
#         self.row = row
#         self.col = col
#
#     def left(self, row, col):
#         return Location(row, col-1)
#
# list_location = [
#     [Location(0, 0), Location(0, 1), Location(0, 2), Location(0, 3)],
#     [Location(1, 0), Location(1, 1), Location(1, 2), Location(1, 3)],
#     [Location(2, 0), Location(2, 1), Location(2, 2), Location(2, 3)],
#     [Location(3, 0), Location(3, 1), Location(3, 2), Location(3, 3)],
# ]
#
#
# class LocationTool:
#     @staticmethod   # 静态方法: 用于定义工具功能
#     def get_location(init_loc, direction, count):
#         '''
#             获取某个方向指定个数的坐标位置
#         :param init_loc: obj, 初始位置对象
#         :param direction: obj, 获取的方向
#         :param count: int, 个数
#         :return: list,存储获取的位置对象
#         '''
#         list_loc = []
#         for i in range(count):
#             init_row = init_loc.row
#             init_col = init_loc.col
#             new_loc = direction(init_row, init_col-i)
#             list_loc.append(new_loc)
#         return list_loc
#
# init_loc = Location(0, 3)
# # 调用静态方法
# list_new_loc = LocationTool.get_location(init_loc, init_loc.left, 2)
# for loc in list_new_loc:
#     print(loc.row, loc.col)
#
# init_loc = Location(0, 2)
# list_new_loc = LocationTool.get_location(init_loc, init_loc.left, 2)
# for loc in list_new_loc:
#     print(loc.row, loc.col)


class ComplateHelper:
    @staticmethod
    def add(number1, number2):
        return number1 + number2

    @staticmethod
    def sub(number1, number2):
        return number1 - number2

# c01 = ComplateHelper()
# print(c01.add(1, 2))

print(ComplateHelper.add(1, 2))
print(ComplateHelper.sub(1, 2))
