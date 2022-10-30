from typing import List

from dal import RestaurantDao
from dtl import RestaurantModel


class RestaurantController:
    """
        餐厅控制器:对核心功能进行逻辑处理,存储/移除..
    """

    def __init__(self):
        self.__dao = RestaurantDao()
        self.list_restaurant = self.__dao.datas # type:List[RestaurantModel]
        if len(self.list_restaurant) ==0:
            self.__start_id = 1001
        else:
            self.__start_id = self.list_restaurant[-1].rid + 1

    def add_commodity(self, new:RestaurantModel)->None:
        """
            添加餐厅
        :param new: 新餐厅对象
        """
        self.list_restaurant.append(new)
        #new.rid = self.__start_id
        self.__start_id += 1
        self.__dao.save()

    def remove_restaurant(self, rid:int)->bool:
        if rid in self.list_restaurant:
            self.list_restaurant.remove(rid)  # 内部:循环执行__eq__
            self.__dao.save()
            return True
        return False

    def update_commodity(self, model:RestaurantModel)->bool:
        for item in self.list_restaurant:
            if item.rid == model.rid:
                item.__dict__ = model.__dict__
                self.__dao.save()
                return True
        return False
