"""
    当前文件:day17/demo08.py
        路径重命名
"""
from pathlib import Path

# 如果旧文件不存在会报错
# Path("a.txt").rename("aa.TXT")

# 目录中的文件重命名
old = Path("b","B.txt")
# 保持路径不变,修改文件名
new = old.with_name("b.txt")
old.rename(new)
