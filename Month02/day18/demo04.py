"""
    类型标注
        背景:
            因为Python变量没有类型,
            所以参数、返回值等都没有类型.

            没有类型就意味着没有操作提示
        定义：
            给变量增加类型的注释
        作用：
            在pycharm中具有操作提示
            可以类型检测
        语法
            参数名:类型
            def 函数名() -> 返回值类型
            变量 = 数据 # type:类型

        复杂类型标注
            from typing import List

            List[类型]  Tuple[类型] ...
            类型1 | 类型2
"""
from typing import List


def func01(p: str):
    print(p.lower())  # 操作提示


def func02() -> int:
    return 10.2


# func01(1001) # 类型检测

class A:
    def __init__(self, data):
        self.data = data  # type:str


a = A("A")

list01 = []  # type:List[str]
list02 = []  # type:List[str | int]

import time

time.mktime((2022, 9, 26, 0, 0, 0, 0, 0, 0))
time.mktime(time.localtime())
