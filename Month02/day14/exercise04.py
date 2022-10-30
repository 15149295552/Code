"""
# 练习1：定义函数,在列表中找出所有偶数
#  [43,43,54,56,76,87,98]

# 练习2：定义函数,在列表中找出所有数字
#  [43,"悟空",True,56,"八戒",87.5,98]
"""


def find_all_even(list_target):
    for item in list_target:
        if item % 2 == 0:
            yield item

def find_all_number(list_target):
    for item in list_target:
        # if type(item) == int or type(item) == float:
        if type(item) in (int, float):
            yield item

list01 = [43, 43, 54, 56, 76, 87, 98]
# print(find_all_even(list01))
for item in find_all_even(list01):
    print(item)


list02 = [43,"悟空",True,56,"八戒",87.5,98]
for item in find_all_number(list02):
    print(item)
