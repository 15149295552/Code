"""
    练习： 获取项目中所有python代码字符数
"""
from pathlib import Path

total_count = 0
for item in Path.cwd().parent.rglob("*.py"):
    with open(item,"r",encoding="utf-8") as file_object:
        total_count += len(file_object.read())
print(total_count)




