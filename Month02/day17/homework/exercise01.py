"""
2. 使用高阶函数操作餐厅列表
    -- 获取所有餐厅名称与人均消费
    -- 获取点评人数大于1000的餐厅
    -- 获取上海餐厅名称
    -- 获取北京最贵餐厅
    -- 获取点评人数最高的3家餐厅(根据点评人数排序)
"""


class Restaurant:
    def __init__(self, city, name, remark, money):
        self.city = city
        self.name = name
        self.remark = remark
        self.money = money

    def __str__(self):
        return str(self.__dict__)


list_restaurant = [
    Restaurant("北京", "星期五餐厅", 2847, 180),
    Restaurant("北京", "铁木真", 3497, 104),
    Restaurant("杭州", "澳门豆捞", 903, 149),
    Restaurant("杭州", "蒙太祖碳烤羊腿", 37, 230),
    Restaurant("上海", "皇轶庭", 421, 110),
    Restaurant("上海", "随缘蒸汽海鲜坊", 682, 128),
]
# 映射
for item in map(lambda r: (r.name, r.money), list_restaurant):
    print(item)

# 过滤
for item in filter(lambda r: r.remark > 1000, list_restaurant):
    print(item)

print(list(map(lambda r: r.name, filter(lambda r: r.city == "上海", list_restaurant))))

# 最大
print(max(filter(lambda r: r.city == "北京", list_restaurant), key=lambda r: r.money))

# 排序
list_restaurant.sort(key = lambda r:r.remark)
list_result = list_restaurant[-3:]
print(list_result) # 加断点
print(sorted(list_restaurant,key = lambda r:r.remark)[-3:])


