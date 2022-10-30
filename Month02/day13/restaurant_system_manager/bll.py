class RestaurantController:
    """
        餐厅控制器:对核心功能进行逻辑处理,存储/移除..
    """

    def __init__(self):
        self.list_restaurant = []
        self.__start_id = 1001

    def add_commodity(self, new):
        """
            添加餐厅
        :param new: 新餐厅对象
        """
        self.list_restaurant.append(new)
        new.rid = self.__start_id
        self.__start_id += 1

    def remove_restaurant(self, rid):
        # for i in range(len(self.list_restaurant)):
        #     # 判断元素的rid
        #     if self.list_restaurant[i].rid == rid:
        #         # 删除元素
        #         del self.list_restaurant[i]
        #         return True
        # return False
        if rid in self.list_restaurant:
            self.list_restaurant.remove(rid)  # 内部:循环执行__eq__
            return True
        return False

    def update_commodity(self, model):
        for item in self.list_restaurant:
            if item.rid == model.rid:
                item.__dict__ = model.__dict__
                return True
        return False
