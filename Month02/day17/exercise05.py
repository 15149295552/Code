"""
    当前文件:month01/exercise05
    当前路径:month01

    -- 打印所有图片的大小
    -- 打印day03中所有练习的路径
    -- 打印所有文本(.txt)文件的创建时间(格式：年/月/日)
"""
from pathlib import Path
import time

for item in Path.cwd().rglob("*.jpg"):
    print(item.stat().st_size)
#
for item in Path.cwd().glob("day03/exercise*"):
    print(item)
#
for item in Path.cwd().rglob("*.txt"):
    tuple_time = time.localtime(item.stat().st_ctime)
    print(item, time.strftime("%Y/%m/%d", tuple_time))

# 扩展：获取大小大于200000的图片名称
result = list(
    map(lambda f: f.name,
        filter(lambda j: j.stat().st_size > 200000,
               Path.cwd().rglob("*.jpg")
               )
        )
)
print(result)
