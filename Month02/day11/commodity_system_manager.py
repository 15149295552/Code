"""
    商品信息管理系统
        餐厅架构
            服务员    传菜员     厨师

        软件架构
            视图View   模型Model   控制器Controller

    餐厅信息管理系统restaurant_system_manager
    练习1:搭建MVC架构
        View:显示菜单、选择菜单、1键录入餐厅信息(北京/星期五餐厅/2847/180)
        Model:city、name、remark、money
        Controller:添加餐厅信息

    练习2:添加餐厅信息
        Model:rid
        Controller:添加餐厅信息(加到列表,设置编号)

    练习3:显示所有餐厅信息
        View:输入2键,打印所有餐厅信息


    练习4:删除餐厅信息
        View:输入3键,获取编号传递给controller再判断成败
        controller:循环列表,删除元素

    练习4:修改餐厅信息
        View:输入4键,获取信息传递给controller再判断成败
        controller:循环列表,修改信息

    练习5:封装餐厅信息管理系统
        View:只提供main
        controller:隐藏start_id
"""


class CommodityView:
    """
        商品视图:对界面进行逻辑处理,输入/输出..
    """

    def __init__(self):
        self.__controller = CommodityController()

    def main(self):
        """
            主要/入口
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_menu(self):
        print("1键输入信息")
        print("2键显示信息")
        print("3键删除信息")
        print("4键修改信息")

    def __select_menu(self):
        number = input("请选择:")
        if number == "1":
            # 重点1:同类调用
            self.__input_commodity()
        elif number == "2":
            self.__display_commoditys()
        elif number == "3":
            self.__delete_commodity()
        elif number == "4":
            self.__modify_commodity()

    def __input_commodity(self):
        # 重点2:每次录入新商品信息作为新商品对象
        cmd = CommodityModel()
        cmd.name = input("请输入商品名称:")
        cmd.price = int(input("请输入商品单价:"))
        # 重点3:每次录入新商品需要添加到旧商品控制器中
        self.__controller.add_commodity(cmd)
        print("噢耶~添加成功啦~")

    def __display_commoditys(self):
        for item in self.__controller.list_commodity:
            print(f"{item.name}的单价是{item.price},编号是{item.cid}")

    def __delete_commodity(self):
        cid = int(input("请输入需要删除的商品编号:"))
        if self.__controller.remove_commodity(cid):
            print("删除成功啦~")
        else:
            print("噢~不~失败啦~")

    def __modify_commodity(self):
        cmd = CommodityModel()
        cmd.cid = int(input("请输入需要修改的商品编号:"))
        cmd.name = input("请输入商品新名称:")
        cmd.price = int(input("请输入商品新单价:"))
        if self.__controller.update_commodity(cmd):
            print("修改成功")
        else:
            print("修改失败")


class CommodityModel:
    """
        商品模型：对多个商品信息进行封装
    """

    def __init__(self, name="", price=0, cid=0):
        self.name = name
        self.price = price
        self.cid = cid  # 全球唯一标识符


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
        for i in range(len(self.list_commodity)):
            if self.list_commodity[i].cid == cid:
                del self.list_commodity[i]
                return True  # 成功
        return False  # 失败

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


view = CommodityView()
view.main()
