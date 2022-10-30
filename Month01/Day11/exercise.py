# 练习：创建2个模块module_exercise.py与exercise.py
# ​    将下列代码粘贴到module_exercise模块中，并在exercise中调用。

# 方法1
# import module_exercise as me
#
# print(me.data)
# me.func01()
# me.MyClass.func03()

# 方法2
# from Day11 import module_exercise as me
#
# print(me.data)
# me.func01()
# me.MyClass.func03()

# from Day11.module_exercise import data
#
# print(data)

# 方法3
# from Day11.module_exercise import *
#
# print(data)
# func01()