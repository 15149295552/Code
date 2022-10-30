from model import EpidemicModel


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
        # for i in range(len(self.list_epidemic)):
        #     if self.list_epidemic[i].eid == eid:
        #         del self.list_epidemic[i]
        #         return True
        # return False
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


# 测试用例
if __name__ == "__main__":
    controller = EpidemicController()
    controller.add_epidemic(EpidemicModel())
    controller.add_epidemic(EpidemicModel())
    controller.add_epidemic(EpidemicModel())
    for item in controller.list_epidemic:
        print(item)
