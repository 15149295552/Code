from dal import HouseDao


class HouseController:
    """
        房源控制器:对核心功能进行逻辑处理,存储/移除..
    """

    def __init__(self):
        self.__dao = HouseDao()
        self.list_house = self.__dao.datas

    def get_max_total_price(self):
        # 方案1:重写Model类的__gt__
        # 优点：最简单
        # 缺点：不灵活
        # return max(self.list_house)

        # 方案2:lambda
        # 优点：最灵活
        # 缺点：最麻烦(每次都需要重写定义)
        return max(self.list_house, key=lambda h: h.total_price)

    def get_order_by_area(self):
        return sorted(self.list_house, key=lambda h: h.area)
