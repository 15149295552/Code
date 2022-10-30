from bll import RestaurantController
from dtl import RestaurantModel


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
        model.remark = self.__get_number("请输入点评人数:")
        model.money = self.__get_number("请输入人均消费:")
        self.__controller.add_commodity(model)
        print("添加成功喽~")

    def __display_restaurants(self):
        for item in self.__controller.list_restaurant:
            # print(f"{item.name}在{item.city},编号是{item.rid},点评人数{item.remark},人均消费{item.money}")
            # 内部:item.__str__()
            print(item)

    def __delete_restaurant(self):
        rid = self.__get_number("请输入餐厅编号:")
        if self.__controller.remove_restaurant(rid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_restaurant(self):
        model = RestaurantModel()
        model.rid = self.__get_number("请输入编号:")
        model.city = input("请输入城市:")
        model.name = input("请输入店名:")
        model.remark = self.__get_number("请输入点评人数:")
        # model.money = int(input("请输入人均消费:"))
        model.money = self.__get_number("请输入人均消费:")
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

    def __get_number(self, message):
        while True:
            try:
                number = int(input(message))
                return number
            except:
                pass
