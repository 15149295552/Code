"""
    字符串字面值
"""

# 1.各种写法
# -- 双引号
data01 = "悟空"
# -- 单引号
data02 = '悟空'

# -- 三引号:可见即所得
data03 = '''悟空'''
data03 = """
    悟
空"""
print(data03)

# 2. 引号冲突
message = '我是"花果山"水帘洞美猴王孙悟空'
message = "我是'花果山'水帘洞美猴王孙悟空"
message = """我是'花果山'水帘洞"美猴王"孙悟空"""

# 3.转义字符:改变字符的原始含义。
# \"   \'   换行\n
message = "我是\"花果山\"水帘洞美猴王\n孙悟空"
print(message)

# 4. 格式化字符串:让字符串按照某种格式显示
# 字符串格式%(数据)
# %s  %d  %f
usd = 16
cny = usd * 6.8902
# print(str(usd) + "美元 = " + str(cny) + "人民币")
print("%s美元 = %s人民币" % (usd, cny))

cure_ratio = 96.8
# print("治愈比例为" + str(cure_ratio) + "%")
# 如果显示1个百分号,需要填写2个
# 如果括号中只有1个数据，可以省略
print("治愈比例为%s%%" % cure_ratio)

jin = 6
liang = 4
# print("结果为：" + str(jin) + "斤" + str(liang) + "两")
print("结果为：%s斤%s两" % (jin, liang))

# %s原样输出
print("%s" % 1.23456789)
# %f "四舍五入"
print("%.0f" % 1.93456789)  #
print(int(1.93456789))  # 向下取整
# %d 整数保留宽度(在左侧用0填充)
print("%.2d" % 5) # 05
print("%.2d:%.2d"%(14,0))
