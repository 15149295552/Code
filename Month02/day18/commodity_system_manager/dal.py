"""
    数据访问层
"""
from pathlib import Path

from dtl import CommodityModel


class CommodityDao:
    """
        商品数据访问对象
    """

    def __init__(self):
        self.file_name = "commoditys.txt"
        # 创建文件
        Path(self.file_name).touch()
        self.datas = []

    def save(self):
        """
            将内存中列表datas保存在硬盘file_name文件中
        """
        with open(self.file_name, "w", encoding="utf-8") as file_object:
            line = self.datas.__repr__()
            file_object.write(line)

    def load(self):
        """
            将硬盘file_name文件加载到内存列表datas中
        """
        with open(self.file_name, "r", encoding="utf-8") as file_object:
            content = file_object.read()
            if content == "":
                self.datas = []
            else:
                self.datas = eval(content)
        return self.datas
