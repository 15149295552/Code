"""
    数据类型
        Python语言变量没有类型
        但是关联的数据有明确的类型
"""
# 1. 字符串 str:存储文本
name = "悟空"
print("1" + "1")  # 11
# 2. 整型 int:存储整数
age = 6
print(1 + 1)  # 2
# 3. 浮点型 float:存储小数
score = 93.5
print(1 + 1.2)  # 2.2
# 注意:字符串不能与数值运算
# print("1" + 1)

# 4. 类型转换
# 结果 = 目标类型(待转数据)
# input函数的结果一定是字符串
age = int(input("请输入年龄:"))
print("明年您"+str(age +1)+"岁了")

# str  -> int
data01 = int("6")
# int  -> str
data02 = str(6)

# str  -> float
data03 = float("6.6")
# float  -> str
data04 = str(6.6)

# int  -> float
data05 = float(6)
# float  -> int
data06 = int(6.1)  # 向下取整
print(data05)  # 6.0
print(data06)  # 6

# print(int("6.1")) # 报错
# print(float("6.+")) # 报错
