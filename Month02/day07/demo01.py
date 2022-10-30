"""

"""
# 疫情信息
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
# --打印第一条疫情信息,
#    格式：xx地区新增xx人,现有xx人,累计xx人
item = list_epidemic[0]
print("%s地区新增%s人,现有%s人,累计%sx人"%
      (item["region"],item["new"],
       item["now"],item["total"]))
# 练习1:
# --打印所有疫情信息,
# --查找新增人数大于10的地区名称(将结果存入新列表)