class RestaurantModel:
    """
        餐厅模型：对多个餐厅信息进行封装
    """

    def __init__(self, city="", name="", remark=0, money=0, rid=0):
        self.city = city
        self.name = name
        self.remark = remark
        self.money = money
        self.rid = rid

    def __str__(self):
        return f"{self.name}在{self.city},编号是{self.rid},点评人数{self.remark},人均消费{self.money}"

    def __eq__(self, other):
        return self.rid == other
