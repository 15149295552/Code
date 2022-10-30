# if 语句

# # 结构1：if语句
# # 适用性：仅判断一种情况
# # 需求：判断年龄，0-18岁，未成年人
# age = int(input('请输入年龄：'))
#
# if 0 <= age <= 18:
#     # 当if语句后的条件成立（True），则执行
#     print('未成年人')


# # 结构2：if-else语句
# # 适用性：判断2种情况
# # 需求：判断年龄，0-18岁，未成年人, 否则（else），成年人
# age = int(input('请输入年龄：'))
#
# if 0 <= age <= 18:
#     print('未成年人')
# else:  # 当if语句后的条件不成立（False），则执行
#     print('成年人')


# 结构3：if-elif-else语句
# 适用性：判断3种或3种以上的情况
# 注意：if、elif条件互斥（满足其中一个，其他的不执行）
# # 需求：判断年龄，0-18岁，未成年人, 大于18，成年人，否则输入错误
# age = int(input('请输入年龄：'))
#
# if 0 <= age <= 18:
#     print('未成年人')
# elif age > 18:   # else if: (负无穷, 0) + (18, 正无穷)
#     print('成年人')
# else:  # 当if语句后的条件不成立（False），则执行   (负无穷, 0)
#     print('年龄输入错误')

# elif语句可以有多个
# 需求：判断年龄，0-18岁，未成年人, 大于18，成年人，否则输入错误
# age = int(input('请输入年龄：'))
#
# if 0 <= age <= 18:
#     print('成长期')
# elif 18 < age <= 60:
#     print('奋斗期')
# elif age > 60:
#     print('退休期')
# else:  # 当if语句后的条件不成立（False），则执行   (负无穷, 0)
#     print('年龄输入错误')


# 结构4：if真值表达式
# if 45:   # if bool(45):
#     print('45')

# bool：
# 为假：0、0.0、False、None、空容器

# number = int(input('请输入一个数：'))
#
# if number % 2:    # bool(1) --> True
#     print('奇数')


# 结构5：if语句嵌套
# 适用性：分类判断，再判断
# age = int(input('请输入一个年龄：'))
#
# if age > -1:  # 年龄值正确
#     if age <= 18:
#         print('未成年人')
#     else:
#         print('成年人')
# else:  # 年龄值错误
#     print('年龄值错误')


# 结构6：if条件表达式
# 适用性：简单的2种情况判断
# 需求：
number = int(input('请输入一个数：'))
if number > 0:
    print('正确')
else:
    print('错误')

print('正确' if number > 0 else '错误')
print('零' if number == 0 else '正数' if number > 0 else '负数')