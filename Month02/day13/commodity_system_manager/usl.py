"""
    用户显示层 user show layer
"""
from bll import CommodityController
from dtl import CommodityModel


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
        # cmd.price = int(input("请输入商品单价:"))
        cmd.price = self.__get_number("请输入商品单价:")
        # 重点3:每次录入新商品需要添加到旧商品控制器中
        self.__controller.add_commodity(cmd)
        print("噢耶~添加成功啦~")

    def __str__(self):
        return ""

    def __display_commoditys(self):
        for item in self.__controller.list_commodity:
            # print(f"{item.name}的单价是{item.price},编号是{item.cid}")
            # 内部：print(item.__str__())
            print(item)  # 打印商品对象,重写商品类__str__

    def __delete_commodity(self):
        # cid = int(input("请输入需要删除的商品编号:"))
        cid = self.__get_number("请输入需要删除的商品编号:")
        if self.__controller.remove_commodity(cid):
            print("删除成功啦~")
        else:
            print("噢~不~失败啦~")

    def __modify_commodity(self):
        cmd = CommodityModel()
        # cmd.cid = int(input("请输入需要修改的商品编号:"))
        cmd.cid = self.__get_number("请输入需要修改的商品编号:")
        cmd.name = input("请输入商品新名称:")
        # cmd.price = int(input("请输入商品新单价:"))
        cmd.price = self.__get_number("请输入商品新单价:")
        if self.__controller.update_commodity(cmd):
            print("修改成功")
        else:
            print("修改失败")

    def __get_number(self,message):
        while True:
            try:
                number = int(input(message))
                return number
            except:
                pass
