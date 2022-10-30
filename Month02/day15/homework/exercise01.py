"""

"""
# 定义生成器函数,实现下列功能:
# -- 查找所有名称是3个字的图形
list_graphics = ["圆形", "三角形", "六边形"]
# -- 查找所有金额大于10000的薪资
list_money = [20000, 17000, 8000]
# -- 查找所有小数
list_data = [True, 1.5, 88]


def find_all_len_eq_3():
    for item in list_graphics:
        if len(item) == 3:
            yield item


def find_single_len_eq_3():
    for item in list_graphics:
        if len(item) == 3:
            return item


def find_all_gt_1w():
    for item in list_money:
        if item > 10000:
            yield item


def find_single_gt_1w():
    for item in list_money:
        if item > 10000:
            return item


def find_all_float():
    for item in list_data:
        if type(item) == float:
            yield item

def find_single_float():
    for item in list_data:
        if type(item) == float:
            return item


# ----------------------------


# 通过for循环调用生成器函数
for item in find_all_len_eq_3():
    print(item)

print(find_single_len_eq_3())

# 通过list()调用生成器函数
list_result = list(find_all_gt_1w())
print(list_result[0])
print(list_result[0])
