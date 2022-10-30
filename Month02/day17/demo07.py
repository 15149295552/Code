"""
    当前文件:day17/demo07.py
        创建路径(文件/目录)
"""
from pathlib import Path

# 创建文件
Path("a.txt").touch()
Path("homework", "b.txt").touch()
# 注意:文件路径必须存在
# Path("a","c.txt").touch()

# 创建目录
# 注意:目录存在就报错
# Path("a").mkdir()
# 目录存在也不报错
Path("a").mkdir(exist_ok=True)
# 目录b不存在就不能创建目录c
# Path("b","c").mkdir(exist_ok=True)