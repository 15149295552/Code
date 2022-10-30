"""
    练习：创建手机类，实例化两个对象并调用其函数，最后画出内存图。
        数据：品牌、价格、颜色
        行为：通话
"""


# 注意
# 类命名方式：所有单词首字母大写,不用下划线隔开
class MobilePhone:
    def __init__(self, brand, price, color="白色"):
        self.brand = brand
        self.price = price
        self.color = color

    def call(self):
        print(self.brand, "在通话")


hua_wei = MobilePhone("华为", 7000, "黑色")
iphone = MobilePhone("苹果", 8000)
hua_wei.call()
iphone.call()
