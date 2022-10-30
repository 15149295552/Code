"""
    数据访问层
"""
from dtl import HouseModel


class HouseDao:
    """
        数据访问对象:负责数据的持久化处理
    """

    def __init__(self):
        self.file_name = "house.txt"
        self.datas = self.load()

    def load(self):
        """
            加载
        """
        with open(self.file_name, "r", encoding="utf-8") as file:
            content = file.read()
            if content == "":
                return []
        return eval(content)
