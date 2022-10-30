'''
练习2：从终端中录入：位移、时间、初速度，计算：加速度
匀变速直线运动的速度与位移公式：
位移 = 初速度 × 时间 + 加速度 * 时间的平方 / 2

效果：
请输入距离：100
请输入初速度：6
请输入时间：10
加速度是：0.8

加速度 = (位移 - 初速度 * 时间) * 2 / 时间 ** 2
'''

# 1 获取数据
distance = float(input('请输入距离：'))
init_speed = float(input('请输入初速度: '))
time = float(input('请输入时间：'))

# 2 数据计算
speed = (distance - init_speed * time) * 2 / time ** 2

# 保留指定的位数
speed = round(speed, 2)

# 3 显示结果
print('加速度是：', speed)