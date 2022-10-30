# 练习2：
#
# 在终端中循环录入5个成绩,
# 最后打印平均成绩(总成绩除以人数)
#
# 效果：
# 请输入成绩：98
# 请输入成绩：83
# 请输入成绩：90
# 请输入成绩：99
# 请输入成绩：78
#
# 平均分：89.6

'''
分析:
    1 循环录入
        while：
            初始条件：count = 0
            循环条件：count < 5
            变化条件：count += 1

        录入：
            score = int(input('请输入一个成绩：'))

    2 累加得到总成绩
        total_score = 0
        while :
            # score += score    --> score = score + score (错误)
            total_score += score

    3 计算平均成绩
        total_score / 5
'''

people = 5
count = 0
total_score = 0
while count < people:
    score = int(input('请输入一个成绩：'))
    total_score += score
    count += 1
else:
    print('总成绩：', total_score)
    avg_score = total_score / people
    print('平均成绩为：', avg_score)