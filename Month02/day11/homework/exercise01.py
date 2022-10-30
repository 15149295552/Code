"""
    -- 定义函数(不在类中),打印所有疫情信息
    -- 定义函数(不在类中),查找新增人数大于10的地区名称(将结果存入新列表)
    -- 定义函数(不在类中),查找现有人数最大的地区信息(结果为字典)
    -- 定义函数(不在类中),根据新增人数对疫情信息降序(大->小)排列
"""


class Epidemic:
    def __init__(self, region, new, now, total):
        self.region = region
        self.new = new
        self.now = now
        self.total = total


# 疫情信息
list_epidemic = [
    Epidemic("台湾", 16, 2339, 16931),
    Epidemic("陕西", 182, 859, 1573),
    Epidemic("浙江", 2, 505, 2008),
]


def print_epidemic_all():
    for item in list_epidemic:
        print(f"{item.region}新增{item.new},现有{item.now},累计{item.total}")


# 查找新增人数大于10的地区名称(将结果存入新列表)
def find_region_new_gt_10():
    list_region = []
    for item in list_epidemic:
        if item.new > 10:
            list_region.append(item.region)
    return list_region


# 查找现有人数最大的地区信息(结果为字典)
def find_max_by_now():
    max_value = list_epidemic[0]
    for i in range(1, len(list_epidemic)):
        if max_value.now < list_epidemic[i].now:
            max_value = list_epidemic[i]
    return max_value


# -- 根据新增人数对疫情信息降序(大->小)排列
def descending_order_by_new():
    for r in range(len(list_epidemic) - 1):
        for c in range(r + 1, len(list_epidemic)):
            if list_epidemic[r].new < list_epidemic[c].new:
                list_epidemic[r], list_epidemic[c] = list_epidemic[c], list_epidemic[r]


descending_order_by_new()
print(list_epidemic)

value = find_max_by_now()
print(value.__dict__)

list_res = find_region_new_gt_10()
print(list_res)

print_epidemic_all()
