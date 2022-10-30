"""
    可变与不可变类型传参的区别
    结论：
        函数内部修改传入的可变数据,
        无需通过return返回结果
"""


def func01(p1, p2):
    p1 = 20 # 修改栈帧中变量,与外界无关
    p2[0] = 20

number = 10
list01 = [10]
func01(number,list01)
print(number) # ？
print(list01) # ？
