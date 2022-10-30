"""
    包
    Python程序结构
    根目录(标记蓝色)
        主模块
        包(文件夹)
            模块1(文件)
            模块2(文件)
                类
                    函数
                        语句
"""
# 路径：从项目根目录开始
# 语法1:"我过去"
# import 路径.模块名 as 别名
# 别名.成员
import package01.package02.module02 as m

m.func01()

# 语法2:"你过来"
# from 路径.模块名 import 成员
# from 路径.模块名 import *
# 直接使用成员
from package01.package02.module02 import *

func01()
func02()












