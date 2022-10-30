"""
    业务逻辑层
"""
class GameController:
    """
        游戏控制器:负责游戏逻辑
    """

    def __init__(self):
        self.__list_merge = None
        self.map = [
            [2, 0, 0, 2],
            [16, 2, 0, 2],
            [2, 4, 2, 4],
            [128, 4, 0, 4],
        ]

    def __zero_to_end(self):
        """
            零元素向后移动
        """
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        """
            对一行合并数据(向左移动的核心算法)
        """
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    def move_left(self):
        """
            向左移动
        """
        for line in self.map:
            self.__list_merge = line
            self.__merge()

    def move_right(self):
        """
            向左移动map
        """
        for line in self.map:  # [2,4,2,2]
            self.__list_merge = line[::-1]  # [2,2,4,2]
            self.__merge()  # [4,4,2,0]
            line[::-1] = self.__list_merge  # [0,2,4,4]

    def __square_matrix_transposition(self):
        """
            方阵转置
        """
        new_map = [list(item) for item in zip(*self.map)]
        self.map[:] = new_map

    def move_up(self):
        """
            向上移动
        """
        self.__square_matrix_transposition()
        self.move_left()
        self.__square_matrix_transposition()

    def move_down(self):
        """
            向下移动
        """
        self.__square_matrix_transposition()
        self.move_right()
        self.__square_matrix_transposition()


if __name__ == '__main__':
    # 测试
    controller = GameController()
    controller.move_down()
    print(controller.map)