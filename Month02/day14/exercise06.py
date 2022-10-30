# 练习：将两个列表合并为一个字典
list_student_name = ["悟空", "八戒", "白骨精"]
list_student_age = [28, 25, 36]

# item 是 ("悟空",28)
# item[0] 是 "悟空"
# item[1] 是 28

# dict_result = {}
# for item in zip(list_student_name, list_student_age):
#     dict_result[item[0]] = item[1]
# print(dict_result)

# dict_result = {item[0]: item[1] for item in zip(list_student_name, list_student_age)}
# print(dict_result)

# dict([("唐", "三藏"), ("猪", "八戒")])
# [("悟空",28),("八戒",25)]
# zip的结果是生成器,可以推算出("悟空",28),("八戒",25)
dict_result = dict(zip(list_student_name, list_student_age))
print(dict_result)
