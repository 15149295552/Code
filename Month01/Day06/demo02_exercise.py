list01 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]]

# 1、将第一行从左到右逐行打印
# for i in list01[0]:
# 	print(i)

# 2、将第二行从右到左逐行打印
# for i in range(len(list01[1])-1, -1, -1):
# 	print(list01[1][i])

# for i in list01[1][::-1]:   # 浅拷贝
# 	print(i)


# 3、将第三列行从上到下逐个打印
# for line in list01:
# 	print(line[2])


# 4、将第四列行从下到上逐个打印
# for i in range(len(list01)-1, -1, -1):
# 	print(list01[i][3])


# 5、将二维列表以表格状打印
# for line in list01:  # line --> 每个小列表
# 	for item in line:  # item --> 小列表中的每个元素
# 		print(item, end='\t')
# 	print()


dict_hobbies = {
    "于谦": ["抽烟", "喝酒", "烫头"],
    "郭德纲": ["说", "学", "逗", "唱"],
}

# 1、打印于谦的所有爱好(一行一个)
# for h in dict_hobbies['于谦']:
#     print(h)

# 2、计算郭德纲所有爱好数量
# print(len(dict_hobbies['郭德纲']))

# 3、打印所有人(一行一个)
# for name in dict_hobbies:
#     print(name)

# 4、打印所有人的爱好(一行一个)
# print(dict_hobbies.values())
#
# for item in dict_hobbies.values():
#     for h in item:
#         print(h)

# for name in dict_hobbies:
#     for h in dict_hobbies[name]:
#         print(h)


dict_travel_info = {
    "北京": {
    	"景区": ["长城", "故宫"],
    	"美食": ["烤鸭", "豆汁焦圈", "炸酱面"]},
  	"四川": {
    	"景区": ["九寨沟", "峨眉山"],
    	"美食": ["火锅", "兔头"]}
}

# 打印北京的第一个景区
# print(dict_travel_info['北京']['景区'][0])

# 打印四川的第二个美食
# print(dict_travel_info['四川']['美食'][1])

# 所有城市 (一行一个)
# for city in dict_travel_info:
#     print(city)

# 北京所有美食(一行一个)
# for food in dict_travel_info['北京']['美食']:
#     print(food)

# 打印所有城市的所有美食(一行一个)
for city in dict_travel_info:
    for food in dict_travel_info[city]['美食']:
        print(food)