# 练习2：定义函数,根据总两数,计算几斤零几两:
# 提示：使用容器包装需要返回的多个数据

def calculate_jin_liang(total_liang):
    '''
        将两数转换为斤和两
    :param total_liang: int, 总两数
    :return: tuple, 计算后的斤和两
    '''
    jin = total_liang // 16
    liang = total_liang % 16
    return jin, liang

total_liang = int(input("请输入两:"))
jin, liang = calculate_jin_liang(total_liang)  # jin, liang = (jin, liang)
print(str(jin) + "斤零" + str(liang) + "两")