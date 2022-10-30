"""
    画出下列代码内存图
"""
import copy

list01 = ["北京",["上海","深圳"]]
list02 = list01 # 赋值:传递地址，数据1份
list03 = list01[:] # 浅拷贝:浅层数据2份,深层数据1份
list04 = copy.deepcopy(list01)# 深拷贝:所有层数据2份

# 修改深拷贝数据,不影响list01
list04[0] = "北京04"
list04[1][1] = "深圳04"
print(list01) # ?

# 修改浅层数据,不影响list01
# 修改深层数据,影响list01
list03[0] = "北京03"
list03[1][1] = "深圳03"
print(list01) # ?

# 修改赋值数据,影响list01
list02[0] = "北京02"
list02[1][1] = "深圳02"
print(list01) # ?