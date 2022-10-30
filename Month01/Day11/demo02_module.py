# 模块 module

# 导入
# 写法1: import
# 如果文件在同一个路径之下,则可以允许此种方法导入
# import modu
#
# print(modu.name)


# 标记: 选中文件夹 --> 右击 Mark Directory as --> Socure Root
# import modu
#
# print(modu.name)
# modu.func()
# modu.Animal.sleep()


# 写法2: from import
# from modu import name, func
# from modu import func

# print(name)
# func()


# 写法3: from xx import *
# from modu import *
#
# print(name)
# func()
# Animal.sleep()


# 命名冲突
# from modu import func
# from modu import *
# import modu

# func()

# def func():
#     print('func')
#
# func()
# modu.func()

'''
    import 模块名    当模块导入较多,避免命名冲突
    from 模块名 import 成员名   导入指定模块中成员较少时
    from 模块名 import *    导入的模块较少时
'''


# 模块的加载过程
# import modu
# from modu import name


# 查看系统路径
import sys

# 查看系统路径
print(sys.path)