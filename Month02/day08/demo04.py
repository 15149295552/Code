def get_iq_score(ma, ca):  # 4
    # iq = ma / ca * 100
    # return iq
    return ma / ca * 100


def calculate_iq_name(ma, ca):  # 2
    score = get_iq_score(ma, ca)  # 3
    if score >= 140:  return "天才"
    if score >= 120:  return "超常"
    if score >= 110:  return "聪慧"
    if score >= 90:   return "正常"
    if score >= 80:   return "迟钝"
    return "低能"


name = calculate_iq_name(25, 22)  # 1
print(name)  # 聪慧
