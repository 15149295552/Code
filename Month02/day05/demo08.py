"""
    元组 基础操作
        创建
        定位(读取)
        遍历(读取)
"""
# 1. 创建
# -- 元组名 = (元素1,元素2,元素3)
tuple_name = ("王乐乐", "梁缘", "张飞")
# -- 元组名 = tuple(可迭代对象)
list_number = [10, 20, 30]
tuple_number = tuple(list_number)

# 2. 定位
# -- 索引
print(tuple_name[0])
# -- 切片
print(tuple_name[-2:])
# 不能修改
# tuple_name[0] = "乐乐"

# 3. 遍历
for item in tuple_number:
    print(item)

# 注意1:元组中只有一个元素,必须加逗号
tuple02 = ("王哲",)
print(tuple02)

# 注意2:在没有歧义的情况下,小括号可以省略
tuple03 = "王哲", "郑德", "李超"
print(tuple03)

# 注意3:序列拆包
a, b, c = tuple03
a, b, c = list_number
a, b, c = "王乐乐"
print(a)
print(b)
print(c)

# 应用:变量交换借助的就是元组
x = 1
y = 2
x, y = (y, x)

# 小心:小心数据后有逗号
name = input("请输入姓名："),
print(name)
