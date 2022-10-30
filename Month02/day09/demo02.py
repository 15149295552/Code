"""
    函数参数
        实际参数
"""
def func01(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)

# 序列实参：将一个序列拆分为多个参数
list01 = [1,2,3]
tuple01 = (1,2,3)
str01 = "孙悟空"
func01(*list01)
func01(*tuple01)
func01(*str01)
# 字典实参：将一个字典拆分为多个参数
dict01 = {"p1":1,"p2":2,"p3":3}
func01(**dict01)
