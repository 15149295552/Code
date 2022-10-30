"""
    当前路径:month01
    搜索目录
"""
from pathlib import Path

# 搜索当前目录所有路径(一层)
# for item in Path.cwd().iterdir():
#     print(item)

# 根据通配符搜索当前目录所有路径(一层)，*表示任意多个字符
# for item in Path.cwd().glob("day03/内存图*"):
#     print(item)

# 根据通配符递归搜索当前目录所有路径(多层)
# for item in Path.cwd().rglob("*.py"):
#     print(item)

# 排序
for item in sorted(
        Path.cwd().rglob("*.py"),
        key=lambda p: p.stat().st_ctime
):
    print(item)
