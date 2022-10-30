"""
    业务逻辑层 business logic layer
"""
from dal import CommodityDao
from dtl import CommodityModel


class CommodityController:
    """
        商品控制器:对核心功能进行逻辑处理,存储/移除..
    """

    def __init__(self):
        self.__dao = CommodityDao()
        self.list_commodity = self.__dao.load()
        if len(self.list_commodity) == 0:
            self.__start_id = 1001
        else:
            self.__start_id = self.list_commodity[-1].cid + 1

    def add_commodity(self, new):
        """
            添加商品
        :param new: 新商品对象
        """
        new.cid = self.__start_id  # 自增长
        self.__start_id += 1
        self.list_commodity.append(new)
        self.__dao.save()

    def remove_commodity(self, cid):
        """
            移除商品信息
        :param cid: int类型,商品编号
        :return: bool类型,是否删除成功
        """
        if cid in self.list_commodity:
            self.list_commodity.remove(cid)  # 内部:自动执行__eq__
            self.__dao.save()
            return True
        return False

    def update_commodity(self, cmd):
        """

        :param cmd:
        :return:
        """
        for item in self.list_commodity:
            if item.cid == cmd.cid:
                item.__dict__ = cmd.__dict__
                self.__dao.save()
                return True
        return False
