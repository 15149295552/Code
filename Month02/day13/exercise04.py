"""
练习：创建函数，在终端中录入int类型成绩。如果格式不正确，重新输入。
效果： score = get_score()
​    print("成绩是：%d"%score)
"""
def get_score():
    while True:
        try:
            score = int(input("请输入成绩："))
            return score # 唯一的出口
        except:
            pass

score = get_score()
print("成绩是：%d" % score)
# 练习:对餐厅信息管理系统做异常处理