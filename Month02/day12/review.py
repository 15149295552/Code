"""
    继承
        行为
            class 爸爸:
                def 功能1(self):

            class 儿子(爸爸):
                def 功能2(self):
                    self.功能1()

            小胖 = 儿子()
            小胖.功能1()
            小胖.功能2()

        数据
            class 爸爸:
                def __init__(self,爸爸参数):
                    self.爸爸数据 = 爸爸参数

            class 儿子(爸爸):
                def __init__(self,爸爸参数,儿子参数):
                    super().__init__(爸爸参数)
                    self.儿子数据 = 儿子参数

            小胖 = 儿子()
            小胖.爸爸数据
            小胖.儿子数据

        关于构造函数：
            -- 子类没构造函数,直接使用父类的
            -- 子类有构造函数,覆盖父类的,此时子类必须通过super调用父类构造函数
"""
