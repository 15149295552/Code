"""
    练习1：创建计算治愈比例的函数
    confirmed = int(input("请输入确诊人数:"))
    cure = int(input("请输入治愈人数:"))
    cure_rate = cure / confirmed * 100
    print("治愈比例为" + str(cure_rate) + "%")
"""


def calculate_cure_ratio(confirmed, cure):
    """
        计算治愈比例
    :param confirmed:
    :param cure:
    :return:
    """
    cure_rate = cure / confirmed * 100
    return cure_rate  # 98.95


confirmed = 96
cure = 95
rate = calculate_cure_ratio(confirmed, cure)
print(rate)
