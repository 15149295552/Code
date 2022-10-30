"""
    根据父母身高,预测儿子身高.
    公式:(父亲身高+母亲身高)*0.54
"""
# 1.获取数据
father_height = float(input("请输入父亲的身高（厘米）:"))
mother_height = float(input("请输入母亲的身高（厘米）:"))
# 2.逻辑计算
son_height = (father_height + mother_height) * 0.54
# 3.显示结果
# 因为需要字符串与数值拼接,所以数值转换为字符串str(son_height)
print("预测儿子的身高是:" + str(son_height) + "厘米")
# 因为直接输出数值,所以不用转换.
print(son_height)

