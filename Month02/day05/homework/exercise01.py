"""
    练习：根据下列文字，提取变量，使用字符串格式化打印信息
    湖北确诊67802人,治愈63326人,治愈率0.99
"""
region = "湖北"
confirmed = 67802
cure = 63326
print("%s确诊%s人,治愈%s人,治愈率%.2f%%" % (region, confirmed, cure, cure / confirmed * 100))
print(f"{region}确诊{confirmed}人,治愈{cure}人,治愈率{cure / confirmed * 100:.2f}%")

total_second = 70
print("%s秒是%.2d分零%.2d秒" % (total_second, total_second // 60, total_second % 60))
print(f"{total_second}秒是{total_second // 60:02}分零{total_second % 60:02}秒")

jin = 6
liang = 7
# print("结果为：" + str(jin) + "斤" + str(liang) + "两")
print("结果为：%s斤%s两" % (jin, liang))
print(f"结果为：{jin}斤{liang}两")

