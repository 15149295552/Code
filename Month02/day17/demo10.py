"""
    读取文件
"""
# 传统代码：手动关闭文件
"""
# 1.打开文件
file_object = open("demo01.py","r",encoding="utf-8")
try:
    # 2.操作文件(可能出错)
    # -- 读取全部
    content = file_object.read()
    print(content)
    # -- 按行读取
    # for item in file_object:
    #     print(item) 
finally:
    # 3.关闭文件
    file_object.close()
"""

# with代码：自动关闭
# 1.打开文件
with open("demo01.py","r",encoding="utf-8") as file_object:
    # 2.操作文件(可能出错)
    # -- 读取全部
    content = file_object.read()
    print(content)
    # -- 按行读取
    # for item in file_object:
    #     print(item)

