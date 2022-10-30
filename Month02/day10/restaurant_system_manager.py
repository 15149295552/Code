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
        self.start_id = 1001

    def add_commodity(self, new):
        """
            添加餐厅
        :param new: 新餐厅对象
        """
        self.list_restaurant.append(new)
        new.rid = self.start_id
        self.start_id += 1


class RestaurantView:
    """
        餐厅视图:对界面进行逻辑处理,输入/输出..
    """

    def __init__(self):
        self.controller = RestaurantController()

    def display_menu(self):
        print("1键输入信息")
        print("2键显示信息")
        print("3键删除信息")
        print("4键修改信息")

    def select_menu(self):
        number = input("请选择:")
        if number == "1":
            # 老司机：先调用函数，在自动生成函数
            # 快捷键:atl + 回车
            self.input_restaurant()

    def input_restaurant(self):
        model = RestaurantModel()
        model.city = input("请输入城市:")
        model.name = input("请输入店名:")
        model.remark = int(input("请输入点评人数:"))
        model.money = int(input("请输入人均消费:"))
        self.controller.add_commodity(model)
        print("添加成功喽~")


view = RestaurantView()
while True:
    view.display_menu()
    view.select_menu()
