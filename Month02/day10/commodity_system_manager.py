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
"""


class CommodityModel:
    """
        商品模型：对多个商品信息进行封装
    """

    def __init__(self, name="", price=0,cid = 0):
        self.name = name
        self.price = price
        self.cid = cid # 全球唯一标识符

class CommodityController:
    """
        商品控制器:对核心功能进行逻辑处理,存储/移除..
    """

    def __init__(self):
        self.list_commodity = []
        self.start_id = 1001

    def add_commodity(self, new):
        """
            添加商品
        :param new: 新商品对象
        """
        new.cid = self.start_id # 自增长
        self.start_id += 1
        self.list_commodity.append(new)


class CommodityView:
    """
        商品视图:对界面进行逻辑处理,输入/输出..
    """

    def __init__(self):
        self.controller = CommodityController()

    def display_menu(self):
        print("1键输入信息")
        print("2键显示信息")
        print("3键删除信息")
        print("4键修改信息")

    def select_menu(self):
        number = input("请选择:")
        if number == "1":
            # 重点1:同类调用
            self.input_commodity()
        elif number == "2":
            pass

    def input_commodity(self):
        # 重点2:每次录入新商品信息作为新商品对象
        cmd = CommodityModel()
        cmd.name = input("请输入商品名称:")
        cmd.price = int(input("请输入商品单价:"))
        # 重点3:每次录入新商品需要添加到旧商品控制器中
        self.controller.add_commodity(cmd)
        print("噢耶~添加成功啦~")


view = CommodityView()
while True:
    view.display_menu()
    view.select_menu()


