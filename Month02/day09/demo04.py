"""
    函数参数
"""


# 命名关键字形参:实参必须是关键字实参
# -- 星号元组形参以后
def func01(*args, p1=0):
    print(args)
    print(p1)


# -- 星号以后
def func02(*, p1=0):
    print(p1)


func01(1, 2, p1=3)
func01(p1=3)
func01(1, p1=3)
func01(1)
func02(p1=1)

name = "悟空"
age = 26
score = 96.8
print("%s的年龄是%s,成绩是%s" % (name, age, score))

print(name, "的年龄是", age, ",成绩是", score,sep = "")

# 在一行中输出
print("*",end = " ")
print("*",end = " ")
print("*",end = " ")
