"""
    while 循环
        while Ture:
            循环体
            if 条件:
                break
"""
# 死循环:循环条件永远满足
while True:
    if input("请输入性别:") == "男":
        print("您好,先生!")
    else:
        print("您好,女士!")

    if input("请输入e键盘退出:") == "e":
        break  # 跳出循环
