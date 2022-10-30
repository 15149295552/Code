# 需求1：定义函数，在列表中查找奇数
# 需求2：定义函数，在列表中查找能被3或5整除的数字

list01 = [3, 5, 1, 15, 22, 21]

# 1 根据需求定义函数
def find01():
    for num in list01:
        if num % 2 == 1:
            yield num

# print(list(find01()))

def find02():
    for num in list01:
        if num % 3 == 0 or num % 5 == 0:
            yield num


# print(list(find02()))

# 2 提取变化点为函数
def condition01(num):
    return num % 2 == 1

def condition02(num):
    return num % 3 == 0 or num % 5 == 0

# 3 定义通用函数
def find(condition):
    for num in list01:
        if condition(num):
            yield num

# 4 调用函数实现需求
print(list(find(condition01)))
print(list(find(condition02)))