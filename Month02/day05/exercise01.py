"""
    画出下列代码内存图
"""
list01 = ["北京", "上海"]
list02 = list01
list01[0] = "广东"
list03 = list01[:]
list03[-1] = "深圳"
print(list01)  # ?
