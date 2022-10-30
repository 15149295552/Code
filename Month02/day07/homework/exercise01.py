"""
    在终端中获取颜色(RGBA),打印描述信息,否则提示颜色不存在
    "R" -> "红色"
    "G" -> "绿色"
    "B" -> "蓝色"
    "A" -> "透明度"
"""
color = input("请输入颜色(RGBA)：")
dict_color_info = {
    "R": "红色",
    "G": "绿色",
    "B": "蓝色",
    "A": "透明度"
}
# print(dict_color_info[color])
if color in dict_color_info:
    print(dict_color_info[color])
else:
    print("颜色不存在")
