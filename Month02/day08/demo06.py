ma = 25
ca = 22
def get_iq_score():
    return ma / ca * 100

def calculate_iq_name():
    score = get_iq_score()
    if score >= 140:  return "天才"
    if score >= 120:  return "超常"
    if score >= 110:  return "聪慧"
    if score >= 90:   return "正常"
    if score >= 80:   return "迟钝"
    return "低能"
name = calculate_iq_name()
print(name)  # 聪慧
