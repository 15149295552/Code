"""
    数据访问层
"""
from pathlib import Path
from dtl import RestaurantModel


class RestaurantDao:
    """
        数据访问对象:负责数据的持久化处理
    """

    def __init__(self):
        self.file_name = "restaurants.txt"
        Path(self.file_name).touch()
        self.datas = self.load()

    # 读取
    def load(self):
        with open(self.file_name, "r", encoding="utf-8") as file:
            content = file.read()
            if content == "":
                return []
        return eval(content)

    # 保存
    def save(self):
        with open(self.file_name, "w", encoding="utf-8") as file:
            content = self.datas.__repr__()
            file.write(content)
