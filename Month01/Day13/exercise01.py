# 练习：创建函数，在终端中录入int类型成绩。如果格式不正确，重新输入。
# 效果： score = get_score()
# ​      print("成绩是：%d"%score)


def get_score():
    while True:
        try:
            score = int(input('请输入成绩:'))
            if 0 <= score <= 100:
                return score
        except Exception as e:
            print('成绩输入错误:', e)

score = get_score()
print("成绩是：%d" % score)