"""
    练习5：
    根据心理年龄与实际年龄，打印智商等级。
    智商IQ = 心理年龄MA 除以 实际年龄CA 乘以 100
    天才：140以上（包含）
    超常：120-139之间（包含）
    聪慧：110-119之间（包含）
    正常：90-109之间（包含）
    迟钝：80-89之间（包含）
    低能：80以下
"""
# ma = int(input("请输入心理年龄："))
# ca = int(input("请输入实际年龄："))
# iq = ma / ca * 100
# if iq >= 140:
#     print("天才")
# elif 120 <= iq < 140:# 如果能执行到本行,一定小于140,所以无需再次判断
#     print("超常")
# elif 110 <= iq < 120:
#     print("聪慧")
# elif 90 <= iq < 110:
#     print("正常")
# elif 80 <= iq < 90:
#     print("迟钝")
# else:
#     print("低能")


# 连续区间判断：只判断单边
ma = int(input("请输入心理年龄："))
ca = int(input("请输入实际年龄："))
iq = ma / ca * 100
if iq >= 140:
    print("天才")
elif iq >= 120:
    print("超常")
elif iq >= 110:
    print("聪慧")
elif iq >= 90:
    print("正常")
elif iq >= 80:
    print("迟钝")
else:
    print("低能")
