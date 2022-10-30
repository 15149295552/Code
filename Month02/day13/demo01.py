"""
    导入
"""
# 语法1:"我过去"
# import 模块名
# 模块名.成员
# 原理：当前模块记录目标模块地址
# 适用性：面向过程(全局变量、函数)
import module01

module01.func01()
module01.func02()

# 语法2:"你过来"
# from 模块 import 成员
# 直接使用成员
# 原理：目标模块成员,来到当前模块作用域
# 小心:命名冲突
# 适用性：面向对象(类)
from module01 import func01
# from module01 import func02,func03
from module01 import *
from module01 import func03 as f3

func01()
func02()

def func03():
    print("demo01-func03")

func03()
f3()


print(__name__)










