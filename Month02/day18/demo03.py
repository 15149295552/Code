"""
    is 与 对象池
"""
list01 = [10]
list02 = [10]
# 判断两个变量内存地址是否相同
print(list01 is list02)  # False
# print(id(list01) == id(list02))
# 因为列表重写了__eq__,所以根据内容比较
print(list01 == list02)

# 对象池(内存池):每次创建数据,都会在池中判断是否具有相同数据
# 如果有相同,则返回地址；没相同,则开空间创建.
# 具有对象池的数据类型：
#   不可变(int/float/bool/str/tuple,None)
# 优点：节省内存空间
data01 = "悟空"
data02 = "悟空"
print(data01 is data02)  # True

# 15：05 上课
