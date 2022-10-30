"""
    业务逻辑层 business logic layer
"""
from dtl import CommodityModel


class CommodityController:
    """
        商品控制器:对核心功能进行逻辑处理,存储/移除..
    """

    def __init__(self):
        self.list_commodity = []
        self.__start_id = 1001

    def add_commodity(self, new):
        """
            添加商品
        :param new: 新商品对象
        """
        new.cid = self.__start_id  # 自增长
        self.__start_id += 1
        self.list_commodity.append(new)

    def remove_commodity(self, cid):
        """
            移除商品信息
        :param cid: int类型,商品编号
        :return: bool类型,是否删除成功
        """
        # for i in range(len(self.list_commodity)):
        #     if self.list_commodity[i].cid == cid:
        #         del self.list_commodity[i]
        #         return True
        # return False

        #    self        other
        # 列表第一个元素 == cid
        # 列表第二个元素 == cid
        # 列表第三个元素 == cid
        if cid in self.list_commodity:
            self.list_commodity.remove(cid)  # 内部:自动执行__eq__
            return True
        return False

    def update_commodity(self, cmd):
        """

        :param cmd:
        :return:
        """
        # for i in range(len(self.list_commodity)):
        #     if self.list_commodity[i].cid == cmd.cid:
        #         # self.list_commodity[i].name = cmd.name
        #         # self.list_commodity[i].price = cmd.price
        #         self.list_commodity[i].__dict__ = cmd.__dict__
        #         return True
        # return False
        for item in self.list_commodity:
            if item.cid == cmd.cid:
                item.__dict__ = cmd.__dict__
                return True
        return False

# 如果当前模块是主模块,才执行测试
# (项目发布后,当前模块不可能是主模块)
if __name__ == "__main__":
    controller = CommodityController()
    controller.add_commodity(CommodityModel())
    controller.add_commodity(CommodityModel())
    controller.add_commodity(CommodityModel())
    for item in controller.list_commodity:
        print(item)
