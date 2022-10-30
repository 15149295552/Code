from bll import EpidemicController
from model import EpidemicModel


class EpidemicView:
    """
        疫情视图：负责处理疫情信息的界面逻辑
    """

    def __init__(self):
        self.__controller = EpidemicController()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_menu(self):
        print("按1键录入疫情信息")
        print("按2键显示疫情信息")
        print("按3键删除疫情信息")
        print("按4键修改疫情信息")

    def __select_menu(self):
        item = input("请输入选项：")
        if item == "1":
            self.__input_epidemic()
        elif item == "2":
            self.__display_epidemic()
        elif item == "3":
            self.__delete_epidemic()
        elif item == "4":
            self.__modify_epidemic()

    def __input_epidemic(self):
        epidemic = EpidemicModel()
        epidemic.region = input("请输入地区名称：")
        # epidemic.new = int(input("请输入新增人数："))
        epidemic.new = self.__get_number("请输入新增人数：")
        epidemic.now =  self.__get_number("请输入现有人数：")
        epidemic.total =  self.__get_number("请输入累计人数：")
        self.__controller.add_epidemic(epidemic)

    def __display_epidemic(self):
        for item in self.__controller.list_epidemic:
            # print("%s地区编号是%s,新增%s人,现有%s人,累计%s人" % (item.region, item.eid, item.new, item.now, item.total))
            print(item) # print自定义对象时,由model的__str__决定显示风格

    def __delete_epidemic(self):
        eid =  self.__get_number("请输入编号：")
        if self.__controller.remove_epidemic(eid):
            print("成功")
        else:
            print("失败")

    def __modify_epidemic(self):
        epidemic = EpidemicModel()
        epidemic.eid =  self.__get_number("请输入编号：")
        epidemic.region = input("请输入地区名称：")
        epidemic.new =  self.__get_number("请输入新增人数：")
        epidemic.now =  self.__get_number("请输入现有人数：")
        epidemic.total =  self.__get_number("请输入累计人数：")
        if self.__controller.update_epidemic(epidemic):
            print("修改成功")
        else:
            print("修改失败")

    def __get_number(self, message):
        while True:
            try:
                number = int(input(message))
                return number
            except:
                pass
