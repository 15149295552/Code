"""
    Python 函数
        小结
        函数内部修改传入的可变数据,无需通过return返回
"""
# 列表嵌套字典存储表格数据
list_epidemics = [
    {
        "region": "台湾", "now": 4110907,
        "total": 4132429, "death": 4132429,
    },
    {
        "region": "香港", "now": 267931,
        "total": 342359, "death": 9419,
    },
    {
        "region": "澳门", "now": 499,
        "total": 642, "death": 2,
    },
]
# 根据累计人数的范围获取疫情地区名称
"""
del get_regions_by_total(begin,end):
    list_region = []
    for item in list_epidemics:
        if begin <= item["total"] < end:
            list_region.append[item["region")]
            return list_region

regions = get_regions_by_total(100000,5000000)
print(list_region)
"""

def get_regions_by_total(begin,end):
    list_region = []
    for item in list_epidemics:
        if begin <= item["total"] < end:
            list_region.append(item["region"])
    return list_region

regions = get_regions_by_total(100000,5000000)
print(regions)

# 清空所有死亡人数
def clear_death():
    # 读取列表元素
    for item in list_epidemics:
        item["death"] = 0  # 修改字典的值

clear_death()
print(list_epidemics)



# def clear_death(list_target):
#     # 读取列表元素
#     for item in list_target:
#         item["death"] = 0  # 修改字典的值
#
# clear_death(list_epidemics) #
# clear_death(list_epidemics[:])
# print(list_epidemics)





# 函数嵌套调用
def condition_by_region(epidemic):  # 4
    return epidemic["region"] == "香港"

def get_epidemics():  # 2
    for item in list_epidemics:
        if condition_by_region(item):  # 3
            return item

result = get_epidemics()  # 1
print(result)


# 是否存在现有人数相同的疫情信息
def is_repeat_now():
    for r in range(len(list_epidemics) - 1):  # 0     1
        for c in range(r + 1, len(list_epidemics)):  # 1 2   2
            if list_epidemics[r]["now"] == list_epidemics[c]["now"]:
                return True
    return False

# 根据累计人数升序排列
# 函数内部修改可变对象,无需通过return返回结果![](../../AppData/Local/Temp/0ea40b8376ef8157791b928a339ed9c9_tplv-obj.png)
def ascending_order_by_total():
    for r in range(len(list_epidemics) - 1):
        for c in range(r + 1, len(list_epidemics)):
            if list_epidemics[r]["total"] > list_epidemics[c]["total"]:
                list_epidemics[r], list_epidemics[c] = list_epidemics[c], list_epidemics[r]






