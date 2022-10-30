from bll import HouseController


class HouseView:
    """
        房源视图:对界面进行逻辑处理,输入/输出..
    """

    def __init__(self):
        self.__controller = HouseController()

    def main(self):
        """
            主要/入口
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_menu(self):
        print("1键显示所有房源信息")
        print("2键显示总价最高房源")
        print("3键根据面积显示房源")

    def __select_menu(self):
        number = input("请选择:")
        if number == "1":
            self.__display_houses()
        elif number == "2":
            self.__display_max_total_price()
        elif number == "3":
            self.__display_order_by_area()

    def __display_houses(self):
        for item in self.__controller.list_house:
            print(item)

    def __display_max_total_price(self):
        house = self.__controller.get_max_total_price()
        print(house)

    def __display_order_by_area(self):
        for item in self.__controller.get_order_by_area():
            print(item)
