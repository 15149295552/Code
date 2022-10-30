"""
    根据文件内容进行搜索
"""
from pathlib import Path

url = input("请输入需要搜索的文件夹:")
key = input("请输入需要搜索的关键词:")
for item in Path(url).rglob("*.py"):
    with open(item, "r", encoding="utf-8") as file_object:
        if key in file_object.read():
            print(item)
