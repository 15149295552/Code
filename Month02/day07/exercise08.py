"""
练习4：创建函数,计算IQ等级
ma = int(input("请输入你的心里年龄："))
ca = int(input("请输入你的实际年龄："))
iq = ma / ca * 100
if 140 <= iq:
	print("天才")
elif 120 <= iq:
    print("超常")
elif 110 <= iq:
    print("聪慧")
elif 90 <= iq:
    print("正常")
elif 80 <= iq:
    print("迟钝")
else:
    print("低能")
"""
"""
def calculate_iq_name(ma,ca):
    iq = ma / ca * 100 
    if 140 <= iq:
        return "天才"   
    elif 120 <= iq:  # 如果上面条件满足,函数退出;不用el也可以表达互斥
        return "超常"
    elif 110 <= iq:
        return "聪慧"
    elif 90 <= iq:
        return "正常"
    elif 80 <= iq:
        return "迟钝"
    else:
        return "低能" 
"""

def calculate_iq_name(ma, ca):
    iq = ma / ca * 100 # 113.6
    if iq >= 140:  return "天才"
    if iq >= 120:  return "超常"
    if iq >= 110:  return "聪慧"
    if iq >= 90:   return "正常"
    if iq >= 80:   return "迟钝"
    return "低能"

name = calculate_iq_name(25, 22)
print(name) # 聪慧
