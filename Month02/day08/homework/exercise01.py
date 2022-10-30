"""
2. 容器嵌套练习（不考虑函数）
    -- 使用列表字典表达下列数据
    -- 打印所有餐饮信息
        格式:xx在xx城市,点评人数xx,人均消费xx元.
    -- 将人均150元以上的餐厅名称存入列表
    -- 查找点评人数最少的店铺（字典）
    -- 根据人均对列表进行升序排列
    城市	    店名	        点评  	人均
    北京	    星期五餐厅	2847	180
    北京	    铁木真	    3497	104
    杭州	    澳门豆捞	    903	    149
    杭州	    蒙太祖碳烤羊腿 37	    230
    上海	    皇轶庭	    421	    110
    上海	    随缘蒸汽海鲜坊 682	128
"""
list_restaurant = [
    {
        "city": "北京", "name": "星期五餐厅",
        "remark": 2847, "money": 180
    },
    {
        "city": "北京", "name": "铁木真",
        "remark": 3497, "money": 104
    },
    {
        "city": "杭州", "name": "澳门豆捞",
        "remark": 903, "money": 149
    },
    {
        "city": "杭州", "name": "蒙太祖碳烤羊腿",
        "remark": 37, "money": 230
    },
    {
        "city": "上海", "name": "皇轶庭",
        "remark": 421, "money": 110
    },
    {
        "city": "上海", "name": "随缘蒸汽海鲜坊",
        "remark": 682, "money": 128
    }
]

# -- 打印所有餐饮信息
# xx在xx地区,点评人数xx,人均消费xx元.
for item in list_restaurant:
    print("%s在%s地区,点评人数%s,人均消费%s元." % (
        item["name"], item["city"], item["remark"], item["money"]))

# -- 将人均150元以上的餐厅名称存入列表
list_name = []
for item in list_restaurant:
    if item["money"] > 150:
        list_name.append( item["name"] )
print(list_name)

# -- 查找点评人数最少的店铺（字典）
min_value = list_restaurant[0]
for i in range(1, len(list_restaurant)):
    if min_value["remark"] > list_restaurant[i]["remark"]:
        min_value = list_restaurant[i]
print(min_value)

# -- 根据人均对列表进行升序排列
for r in range(len(list_restaurant) - 1):
    for c in range(r + 1, len(list_restaurant)):
        if list_restaurant[r]["money"] > list_restaurant[c]["money"]:
            list_restaurant[r], list_restaurant[c] = list_restaurant[c], list_restaurant[r]
print(list_restaurant)
