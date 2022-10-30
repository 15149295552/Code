"""
    生成器函数-应用
"""
list01 = [43, 54, 56, 7, 76, 87, 98, 9]


# 定义函数,获取所有大于50的数字
# 传统思想:创建列表存储所有结果
# def get_numbers_gt_50():
#     list_result = []
#     for item in list01:
#         if item > 50:
#             list_result.append(item)
#     return list_result
#
# data = get_numbers_gt_50()
# for item in data:
#     print(item)


# 生成器思想:用yield生成数据
def get_numbers_gt_50():
    for item in list01:
        if item > 50:
            yield item


# data存储的是生成器对象地址
data = get_numbers_gt_50()
for item in data:
    print(item)
