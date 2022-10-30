"""
自定义进程类
"""
from time import sleep
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, song):
        self.song = song
        super().__init__()  # 执行父类构造函数

    # 重写父类提供的方法
    def run(self):
        for i in range(3):
            sleep(2)
            print("Playing %s" % self.song)

    # def player(self):
    #     self.start()


if __name__ == '__main__':
    # 创建进程 + 进程要做的事情完成
    music = MyProcess("歌唱祖国")
    music.start()  # 自动运行run



#################  Process 猜想 ########
# class Process:
#     def __init__(self,target=None):
#         self.target = target
#
#     def run(self):
#         self.target()
#
#     def start(self):
#         # 创建进程
#         self.run()








