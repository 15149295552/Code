"""
    当前文件:month01/demo05.py
    当前路径:month01
"""
from pathlib import Path

# 相对路径
p1 = Path("day06", "demo01.py")
print(p1.exists())

# 通过对象访问实例方法(操作自己的数据)
# 通过类名访问类方法(操作大家的数据)
# 当前路径的绝对路径
print(Path.cwd())
# 绝对路径+相对路径
p2 = Path.cwd().joinpath("day06", "demo01.py")
print(p2.exists())

# 路径对象可以访问各种路径信息
print(p1.name)
print(p1.stem)
print(p1.suffix)
print(p2.parts)

import time
#  时间戳 -> 时间元组
print(time.localtime(p2.stat().st_ctime))
