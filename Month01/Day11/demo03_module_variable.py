# 模块变量

from modu import func

# 查看模块中函数的文档字符串
# print(func.__doc__)

# 查看当前模块所在的路径
# print(__file__)

# 查看模块的名字: 如果当前模块是主模块则返回__main__
# 运行哪个模块,哪个模块就是主模块
# print(__name__)

# if __name__ == '__main__':   # 程序执行的入口: 推荐程序执行写在该语句之下
#     print('程序从此处开始调用')

# from pypinyin import pinyin
#
# print(pinyin('达内'))


# 模块使用注意
# 1 自定义模块不要与内置模块或第三方模块重名
# import random
# import sys
#
# print(sys.path)
# print(random.randint(1,10))

# 2 模块名不要用纯数字
# import 111

