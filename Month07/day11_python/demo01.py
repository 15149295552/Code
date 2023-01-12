"""
    模块
"""
# 1."我过去"
# 原理:创建变量存储目标模块地址
# 导入：import 模块名称
# 使用：模块名称.成员
import module01

module01.func01()

# 2."你过来"
# 原理:目标模块的成员加入到当前模块作用域
# 导入:from 模块名称 import 成员
# 使用：直接使用成员
# 注意1：如果需要导入的成员过多, 可以使用星号表示全部
# from module01 import func01,func02
from module01 import *
# 注意2：成员命名可能冲突 
from module01 import func02 as f2

def func02():
    print("demo01 - func02")

func01()
func02()
f2()
