"""
    Python 容器
        --小结
        # 读取全部数据
        for item in 列表:
        # 修改全部数据
        for i in range(len(列表)):
        # 修改列表元素的元素
        for item in 列表:
            item["键"]
"""

# 列表擅长存储单一维度数据
list_name = ["台湾", "香港", "澳门", "内蒙古"]

# 读取全部数据
# for ... 列表
for item in list_name:
    if len(item) == 2:
        print(item)

# 修改全部数据
# for ... range
for i in range(len(list_name)):
    if len(list_name[i]) == 2:
        list_name[i] = ""

# 字典擅长存储多个维度数据
dict_taiwan = {
    "region": "台湾",
    "now": 4110907,
    "total": 4132429,
    "death": 4132429,
}
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
# 查找现有人数最大的疫情信息
max_value = list_epidemics[0]
for i in range(1, len(list_epidemics)):
    if max_value["now"] < list_epidemics[i]["now"]:
        max_value = list_epidemics[i]
print(max_value)

# 累加累计人数
sum_total = 0
for item in list_epidemics:
    sum_total += item["total"]
print(sum_total)

# 读取列表元素,修改元素的元素
for item in list_epidemics:
    item["now"] = 0
