"""
    数据传输层  data transfer layer
"""
class CommodityModel:
    """
        商品模型：对多个商品信息进行封装
    """

    def __init__(self, name="", price=0, cid=0):
        self.name = name
        self.price = price
        self.cid = cid

    def __str__(self):
        return f"{self.name}的单价是{self.price},编号是{self.cid}"

    def __eq__(self, other):
        return self.cid == other
