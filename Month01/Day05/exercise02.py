'''
根据年月日,计算是这一年的第几天.
公式：前几个月总天数 + 当月天数

例如：5月10日
计算：31 29 31 30 + 10

闰年的判断条件：
    1 能被4整除，并且不能被100整除
    2 能被400整除

1 3 5 7 8 10 12月：31天
4 6 9 11：30天
2月：闰年：29天 平年：28天

分析：
    1 获取年、月、日
    2 判断
        1月份:日
        2月份:31 + 日
        超过2月份
            tuple_days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30)
            3月份：31 + 28 + 日
                sum(tuple_days[:month-1])
            4月份：31 + 28 + 31 + 日
                sum(tuple_days[:month-1])
            12月份： 前11月份天数 + 日

        判断闰年
            if year%4==0 and year%100!=0 or year%400==0:
                total_days += 1

    3 定义记录天数
        total_days = 0
'''
# 方法1
# year = int(input('请输入年份：'))
# month = int(input('请输入月份：'))
# day = int(input('请输入天数：'))
#
# if year > 0 and 1 <= month <= 12 and 0 < day < 32:  # 日期正确情况
#     if month == 1:
#         total_day = day
#         # print(f'{year}年{month}月{day}日是{year}年的第{total_day}天')
#     elif month == 2:
#         total_day = 31 + day
#         # print(f'{year}年{month}月{day}日是{year}年的第{total_day}天')
#     else:  # month > 2
#         tuple_days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30)
#         total_day = day
#
#         if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#             total_day += 1
#
#         total_day += sum(tuple_days[:month - 1])
#     print(f'{year}年{month}月{day}日是{year}年的第{total_day}天')
# else:
#     print('日期输入错误')

# # 方法2
# year = int(input('请输入年份：'))
# month = int(input('请输入月份：'))
# day = int(input('请输入天数：'))
if year > 0 and 1 <= month <= 12 and 0 < day < 32:  # 日期正确情况
    tuple_days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30)
    total_day = day

    if month > 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            total_day += 1

    total_day += sum(tuple_days[:month - 1])
    print(f'{year}年{month}月{day}日是{year}年的第{total_day}天')
else:
    print('日期输入错误')


# 方法3
date = input('请输入日期【xxxx/xx/xx】：')
list_date = date.split('/')  # ['2022', '2', '15']
year, month, day = [int(item) for item in list_date]  # [2022, 2, 15]

if year > 0 and 1 <= month <= 12 and 0 < day < 32:  # 日期正确情况
    tuple_days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30)
    total_day = day

    if month > 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            total_day += 1

    total_day += sum(tuple_days[:month - 1])
    print(f'{year}年{month}月{day}日是{year}年的第{total_day}天')
else:
    print('日期输入错误')