"""
    根据下列文字，提取变量，使用字符串格式化打印信息
    湖北确诊67802人,治愈63326人,治愈率0.99
    70秒是01分零10秒
"""
region = "湖北"
confirmed = 67802
cure = 63326
print("%s确诊%s人,治愈%s人,治愈率%.2f%%" % (region, confirmed, cure, cure / confirmed * 100))

number_second = 100
minute = number_second // 60
print("%s秒是%.2d分零%.2d秒" % (number_second, minute, number_second % 60))

subject = "I"
predicate = "kiss"
object = "you"
# print("您输入的主语是:" + subject + ",谓语是:" + predicate + ",宾语是:" + object)
print("您输入的主语是:%s,谓语是:%s,宾语是:%s" % (subject, predicate, object))
