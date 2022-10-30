"""
    面向对象思考流程:
        现实世界       虚拟世界
        车 --抽象化--> 类 --实例化--> 对象
                    颜色            白色
                    车牌            京c007
                    品牌            奔驰

        投影仪
        空调
        桌子

    类:整数、小数、列表...自定义类
    对象:166,1.2、[10]...自定义对象
"""


class Wife:
    def __init__(self, name, height=160, face_score=95):
        # 数据
        self.name = name
        self.height = height
        self.face_score = face_score

    # 行为
    def work(self):
        print(self.name, "在工作")

jian_ning = Wife("建宁", 166, 96)
jian_ning.name = "公主"
jian_ning.work()

shuang_er = Wife("双儿", 120)
shuang_er.work()
