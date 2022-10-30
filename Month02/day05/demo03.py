"""
    画出下列代码内存图
        遍历
"""
list_name = ["杨建宏","马鹏", "潘兴兴","陈亦菲"]
for item in list_name:
    if len(item) == 3:
        print(item)

# for item in list_name:
#     if len(item) == 3:
#         item = ""

for i in range(len(list_name)):
    if len(list_name[i]) == 3:
        list_name[i] = ""

print(list_name)