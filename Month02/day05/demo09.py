"""
    请以容器思想,改造下列代码
    month = int(input("请输入月份："))
    if 1 <= month <= 12:
        if month == 2:
            print("29天")
        elif month == 4 or month == 6 or month == 9 or month == 11:
            print("30天")
        else:
            print("31天")
    else:
        print("月份输入有误")
"""
month = int(input("请输入月份："))
if 1 <= month <= 12:
    if month == 2:
        print("29天")
    # elif month == 4 or month == 6 or month == 9 or month == 11:
    elif month in (4, 6, 9, 11):
        print("30天")
    else:
        print("31天")
else:
    print("月份输入有误")


tuple_day = (31,29,31,30,31,30,31,31,30,31,30,31)
print(tuple_day[0])
print(tuple_day[4])
month = int(input("请输入月份："))
print(tuple_day[month-1])



