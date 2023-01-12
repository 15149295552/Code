"""
    Python程序结构

根目录
    主模块(第一次运行程序的模块)
    包
        模块
            类
                函数
                    语句
"""
# 注意：路径从根目录开始
#
# 导入：import 包.模块 as 别名
# 使用：别名.成员
import package01.package02.module01 as m

m.func01()

# 导入：from 包.模块 import 成员
# 使用：直接使用成员
from package01.package02.module01 import *

func01()
func02()