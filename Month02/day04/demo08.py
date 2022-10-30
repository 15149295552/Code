"""
    列表list
        作用：存储单一维度数据
        基础操作
            创建
            添加
            定位
            删除
            遍历
"""
# 1. 创建
# --列表名 = [元素1,元素2,元素3]
list_name = ["马鹏", "王子依", "陆飞翔"]
list_sex = ["男", "女", "女"]
list_age = [27, 23, 25]
# --列表名 = list(可迭代对象)
list_gyt = list("郭玉涛")
print(list_gyt)
# 2. 添加
# --列表名.append(元素)
list_name.append("贾瑞")
list_age.append(26)
print(list_name)
# --列表名.insert(索引,元素)
list_name.insert(2, "梁缘")
print(list_name)
# 3. 定位
# -- 索引
print(list_name)
print(list_name[1])  # 读取第二个元素
list_name[2] = "老梁"  # 修改第三个元素
# -- 切片
# 读取前两个元素
print(list_name[:2])
# 修改后两个元素
list_name[-2:] = ["陆陆", "瑞瑞"]
# 将年龄列表所有元素归零
# list_age[:] = [0,0,0,0]
# list_age[:] = [0] * 4
list_age[:] = [0] * len(list_age)
print(list_age)
# 4. 删除
# -- 根据定位
del list_name[1]
del list_age[:2], list_sex[-2:]
# -- 根据元素
# 列表名.remove(元素)
# 注意:元素不存在则报错
#     元素存在多个,只会删除第一个
# list_name.remove("老梁")
if "梁哥" in list_name:
    list_name.remove("梁哥")
print(list_name)
# 5. 遍历
# -- 从头到尾读取
#    for item in 列表:
#        item 是列表元素
# 查找叠字的姓名
for item in list_name:
    if item[0] == item[1]:
        print(item)

# -- 从头到尾修改
#    for i in range(len(列表)):
#        i 是列表元素的索引
#        列表[i]是列表元素
list_sex = ["男", "女", "女"]
for i in range(len(list_sex)):  # 0 1 2
    if list_sex[i] == "男":
        list_sex[i] = "女"
    else:
        list_sex[i] = "男"
print(list_sex)
