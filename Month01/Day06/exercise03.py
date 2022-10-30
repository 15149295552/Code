# 练习1：创建计算治愈比例的函数
def calculate_cure_rate(confirmed: int, cure: int) -> float:
    '''
        计算并返回治愈比例
    :param confirmed: int, 确诊人数
    :param cure:int, 治愈人数
    :return:float, 治愈比例
    '''
    # cure_rate = cure / confirmed * 100
    # return cure_rate
    return cure / confirmed * 100

confirmed = int(input("请输入确诊人数:"))
cure = int(input("请输入治愈人数:"))
cure_rate = calculate_cure_rate(confirmed, cure)
print("治愈比例为" + str(cure_rate) + "%")
# calculate_cure_rate(3.4, 5.6)