"""
    列表内存分布
        创建
        定位
"""
list_name = ["马鹏","潘兴兴","陈亦菲"]
data01 = list_name
data02 = list_name[0]
data03 = list_name[:2] # 通过切片读取数据,会创建新列表

data03[1] = "兴兴"
data02 = "鹏鹏"
data01[2] = "菲菲" # 对list_name有影响

print(list_name) # ?