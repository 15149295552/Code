"""
    字典推导式
        根据可迭代对象,简单的构建新字典
"""
# dict_result = {}
# for number in range(1, 11):
#     if number % 3 == 0:
#         dict_result[number] = number ** 2
# print(dict_result)
dict_result = {
    number: number ** 2
    for number in range(1, 11) if number % 3 == 0
}
print(dict_result)
list_name = ["马鹏", "王子依", "陆飞翔"]
list_sex = ["男", "女", "女"]
# dict_person = {}
# for i in range(len(list_name)):
#     key = list_name[i]
#     value = list_sex[i]
#     dict_person[key] = value
# print(dict_person)
dict_person = {list_name[i]: list_sex[i]
               for i in range(len(list_name))}
print(dict_person)

