"""
	--打印北京的第一个景区
	--打印所有城市 (一行一个)
	--打印所有城市的所有美食(一行一个)
"""
dict_travel_info = {
    "北京": {
        "景区": ["长城", "故宫"],
        "美食": ["烤鸭", "豆汁焦圈", "炸酱面"]
    },
    "四川": {
        "景区": ["九寨沟", "峨眉山"],
        "美食": ["火锅", "兔头"]
    }
}
print(dict_travel_info["北京"]["景区"][0])

for key in dict_travel_info:
    print(key)

for value in dict_travel_info.values():
    for item in value["美食"]:
        print(item)
# ---------------
dict_travel_info["北京市"] = dict_travel_info["北京"]
del dict_travel_info["北京"]
print(dict_travel_info)
# 17:01 上课