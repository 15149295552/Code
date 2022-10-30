"""
    用户显示层
"""
from bll import GameController

class GameView:
    """
        游戏视图:负责界面逻辑
    """

    def __init__(self):
        self.__controller = GameController()

    def __display_map(self):
        for line in self.__controller.map:
            for item in line:
                print(item, end="\t")
            print()  # 换行

    def __input_for_move_map(self):
        dir = input("请输入方向(wsad)")
        if dir == "w":
            self.__controller.move_up()
        elif dir == "s":
            self.__controller.move_down()
        elif dir == "a":
            self.__controller.move_left()
        elif dir == "d":
            self.__controller.move_right()

    def main(self):
        while True:
            self.__display_map()
            self.__input_for_move_map()
