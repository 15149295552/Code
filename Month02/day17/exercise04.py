"""
    当前目录：month01
    (3) 练习：在month01目录中，分别使用相对路径、绝对路径判断下列文件是否存在：
    day03/demo01.py
    day03/homework/exercise01.py
    day04/homework/exercise01.py
"""
from pathlib import Path
import  time

# 绝对 + 相对
print(Path.cwd().joinpath("day03","demo01.py").exists())
print(Path.cwd().joinpath("day03","homework","exercise01.py").exists())
# 相对
print(Path("day04","homework","exercise01.py").exists())
p1 = Path("day04","homework","exercise01.py")
