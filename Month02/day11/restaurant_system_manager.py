class RestaurantModel:
    """
        餐厅模型：对多个餐厅信息进行封装
    """

    def __init__(self, city="", name="", remark=0, money=0, rid=0):
        self.city = city
        self.name = name
        self.remark = remark
        self.money = money
        self.rid = rid


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
        for i in range(len(self.list_restaurant)):
            if self.list_restaurant[i].rid == rid:
                del self.list_restaurant[i]
                return True
        return False

    def update_commodity(self, model):
        for item in self.list_restaurant:
            if item.rid == model.rid:
                item.__dict__ = model.__dict__
                return True
        return False


class RestaurantView:
    """
        餐厅视图:对界面进行逻辑处理,输入/输出..
    """

    def __init__(self):
        self.__controller = RestaurantController()

    def __display_menu(self):
        print("1键输入信息")
        print("2键显示信息")
        print("3键删除信息")
        print("4键修改信息")

    def __select_menu(self):
        number = input("请选择:")
        if number == "1":
            # 老司机：先调用函数，在自动生成函数
            # 快捷键:atl + 回车
            self.__input_restaurant()
        elif number == "2":
            self.__display_restaurants()
        elif number == "3":
            self.__delete_restaurant()
        elif number == "4":
            self.__modify_restaurant()

    def __input_restaurant(self):
        model = RestaurantModel()
        model.city = input("请输入城市:")
        model.name = input("请输入店名:")
        model.remark = int(input("请输入点评人数:"))
        model.money = int(input("请输入人均消费:"))
        self.__controller.add_commodity(model)
        print("添加成功喽~")

    def __display_restaurants(self):
        for item in self.__controller.list_restaurant:
            print(f"{item.name}在{item.city},编号是{item.rid},点评人数{item.remark},人均消费{item.money}")

    def __delete_restaurant(self):
        rid = int(input("请输入餐厅编号:"))
        if self.__controller.remove_restaurant(rid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_restaurant(self):
        model = RestaurantModel()
        model.rid = int(input("请输入编号:"))
        model.city = input("请输入城市:")
        model.name = input("请输入店名:")
        model.remark = int(input("请输入点评人数:"))
        model.money = int(input("请输入人均消费:"))
        if self.__controller.update_commodity(model):
            print("修改成功喽~")
        else:
            print("修改失败")

    def main(self):
        """

        """
        while True:
            self.__display_menu()
            self.__select_menu()


view = RestaurantView()
view.main()
