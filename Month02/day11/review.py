"""
    复习 - MVC(控制与显示分离)
        职责:
            View:负责表面(输入/输出)
            Model:负责打包(多合一)
            Controller:负责核心(存储/移除)
        语法:
            class Model:
                def __init__(self,data=0):
                    self.data = data

            class View:
                def __init__(self):
                    self.controller = Controller()

                def func01(self):
                    # 每次用一个新对象
                    model = Model()
                    model.data = input()

                def func02(self):
                     # 每次用旧对象
                     self.controller.func03()

            class Controller:
                def func03(self):
                    pass

            view = View()
"""