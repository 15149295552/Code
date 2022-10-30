"""
    写入文件
"""
# 1. 打开文件
with open("a.txt","a",encoding="utf-8") as file_object:
    print(file_object.write("别睡啦\n"))
    # 2. 写入数据

