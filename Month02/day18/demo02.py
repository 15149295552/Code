"""
    自定义对象持久化存储
"""


class CommodityModel:
    def __init__(self, name="", price=0, cid=0):
        self.name = name
        self.price = price
        self.cid = cid

    def __repr__(self):
        return f'CommodityModel("{self.name}", {self.price}, {self.cid})'

"""
# 原有自定义对象
tld = CommodityModel("屠龙刀", 10000, 1001)
line = tld.__repr__()

# 写入到文件
with open("a.txt", "w", encoding="utf-8") as file_object:
    file_object.write(line + "\n")

# 从文件读取
with open("a.txt", "r", encoding="utf-8") as file_object:
    for line in file_object:
        new = eval(line)
        print(new)
"""

# 自定义对象列表
list_commodity = [
    CommodityModel("屠龙刀", 10000, 1001),
    CommodityModel("金箍棒", 20000, 1002),
]

line = list_commodity.__repr__()

# 写入到文件
with open("a.txt", "w", encoding="utf-8") as file_object:
    file_object.write(line)

# 从文件读取
with open("a.txt", "r", encoding="utf-8") as file_object:
    new = eval(file_object.read())
    print(new[0])
    print(new[1])