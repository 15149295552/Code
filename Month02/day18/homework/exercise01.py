"""
    当前代码：month01/exercise01.py
    当前路径：month01
    在month01目录中,获取所有图片(jpg)路径对象,存储在列表中
    从路径对象列表中找出所有文件名存储新列表
    从路径对象列表中找出所有文件大小存储在新列表中
    从路径对象列表中找出最大的文件 max
    根据大小对路径对象列表进行升序排列 sort
"""

from pathlib import Path

# 从硬盘上搜索文件
list_image = list(Path.cwd().rglob("*.jpg"))
# 在内存中筛选文件
list_file_name = list(map(lambda p: p.name, list_image))
list_file_size = list(map(lambda p: p.stat().st_size, list_image))
# 找到最大的文件
max_file = max(list_image, key=lambda p: p.stat().st_size)
list_image.sort(key=lambda p: p.stat().st_size)
# 找到最大的3个文件
list_max = list_image[-3:]
print(list_max)
