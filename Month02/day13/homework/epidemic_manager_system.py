"""
    疫情信息管理系统
"""


class EpidemicModel:
    """
        疫情模型：包装疫情信息
    """

    def __init__(self, region="", new=0, now=0, total=0, eid=0):
        self.region = region
        self.new = new
        self.now = now
        self.total = total
        self.eid = eid

    # self是列表中的元素,other是编号
    def __eq__(self, other):
        return self.eid == other

    def __str__(self):
        return "%s地区编号是%s,新增%s人,现有%s人,累计%s人" % (self.region, self.eid, self.new, self.now, self.total)


class EpidemicController:
    """
        疫情控制器：负责处理核心逻辑,例如:存储,添加
    """

    def __init__(self):
        self.__start_id = 1001
        self.list_epidemic = []

    def add_epidemic(self, new):
        new.eid = self.__start_id
        self.__start_id += 1
        self.list_epidemic.append(new)

    def remove_epidemic(self, eid):
        if eid in self.list_epidemic:
            self.list_epidemic.remove(eid)
            return True
        return False

    def update_epidemic(self, epidemic):
        for item in self.list_epidemic:
            if item.eid == epidemic.eid:
                item.__dict__ = epidemic.__dict__
                return True
        return False


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
        # 重点1：本类通过self互相访问
        if item == "1":
            self.__input_epidemic()
        elif item == "2":
            self.__display_epidemic()
        elif item == "3":
            self.__delete_epidemic()
        elif item == "4":
            self.__modify_epidemic()

    def __input_epidemic(self):
        # 重点2：View通过跨类调用方式1,访问Model实例变量
        epidemic = EpidemicModel()
        epidemic.region = input("请输入地区名称：")
        epidemic.new = int(input("请输入新增人数："))
        epidemic.now = int(input("请输入现有人数："))
        epidemic.total = int(input("请输入累计人数："))
        # 重点3：View通过跨类调用方式2,访问Controller实例方法
        self.__controller.add_epidemic(epidemic)

    def __display_epidemic(self):
        for item in self.__controller.list_epidemic:
            # print("%s地区编号是%s,新增%s人,现有%s人,累计%s人" % (item.region, item.eid, item.new, item.now, item.total))
            print(item)

    def __delete_epidemic(self):
        eid = int(input("请输入编号："))
        if self.__controller.remove_epidemic(eid):
            print("成功")
        else:
            print("失败")

    def __modify_epidemic(self):
        epidemic = EpidemicModel()
        epidemic.eid = int(input("请输入编号："))
        epidemic.region = input("请输入地区名称：")
        epidemic.new = int(input("请输入新增人数："))
        epidemic.now = int(input("请输入现有人数："))
        epidemic.total = int(input("请输入累计人数："))
        if self.__controller.update_epidemic(epidemic):
            print("修改成功")
        else:
            print("修改失败")


view = EpidemicView()
view.main()
