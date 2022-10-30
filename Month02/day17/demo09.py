"""
    当前文件:day17/demo08.py
        删除路径
"""
from pathlib import Path

# 删除文件
# Path("aa.TXT").unlink()
# Path("b","B.txt").unlink()

# 删除目录
Path("b").rmdir()
