# 3、循环录入多个学生的信息（姓名、年龄、成绩），当姓名输入为空，则结束录入
#     按照：姓名：xxx,年龄：xxx,成绩：xxx 打印结果

'''
    存储结构：{学号: [姓名, 年龄, 成绩]}
            [{'name': xxx, 'age':xx, 'score':xx}, ...]

    1 定义空列表 list_stu
    2 死循环:
        1 输入姓名
            if name == '':
                break
        2 输入年龄、成绩
        3 构建字典存储学生的3个信息
        4 将字典存储至列表中
    3 遍历字典打印数据信息
'''

list_stu = []

while True:
    name = input('请输入姓名：')
    if name == '':
        break
    age = int(input('请输入年龄：'))
    score = int(input('请输入成绩：'))

    # 方法1
    # dict_stu = {}
    # dict_stu['name'] = name
    # dict_stu['age'] = age
    # dict_stu['score'] = score

    # 方法2
    dict_stu = {'name': name, 'age':age, 'score':score}
    list_stu.append(dict_stu)

print(list_stu)

for stu in list_stu:    # stu --> dict
    print(f'姓名：{stu["name"]},年龄：{stu["age"]},成绩：{stu["score"]}')