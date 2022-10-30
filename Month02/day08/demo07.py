"""

"""
# --------------全局变量------------------
list_epidemic = [
    {
        "region": "台湾", "new": 16,
        "now": 2339, "total": 16931,
    },
    {
        "region": "陕西", "new": 182,
        "now": 859, "total": 1573,
    },
    {
        "region": "浙江", "new": 2,
        "now": 505, "total": 2008,
    },
]

# --------------定义函数------------------
# --打印所有疫情信息,
def print_epidemic_all( ):
    for item in list_epidemic:
        print("%s地区新增%s人,现有%s人,累计%s人" % (item["region"], item["new"], item["now"], item["total"]))

# --查找新增人数大于10的地区名称(将结果存入新列表)
def get_regions_by_new(value):
    list_region = []
    for item in list_epidemic:
        if item["new"] > value:
            list_region.append(item["region"])
    return list_region

# --查找现有人数最大的地区信息(结果为字典)
def get_max_epidemic_by_now():
    max_value = list_epidemic[0]
    for i in range(1, len(list_epidemic)):
        if max_value["now"] < list_epidemic[i]["now"]:
            max_value = list_epidemic[i]
    return max_value

# --根据新增人数对疫情信息降序(大->小)排列
def descending_order_by_new():
    for r in range(len(list_epidemic) - 1):
        for c in range(r + 1, len(list_epidemic)):
            if list_epidemic[r]["new"] < list_epidemic[c]["new"]:
                list_epidemic[r], list_epidemic[c] = list_epidemic[c], list_epidemic[r]

# --------------调用函数------------------
print(get_regions_by_new(5))
print(get_regions_by_new(100))
print(get_max_epidemic_by_now())
descending_order_by_new()
print_epidemic_all()