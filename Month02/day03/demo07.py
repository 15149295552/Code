"""
    for  +   range()
"""
# 写法1:
# range(开始,结束,间隔)
# 注意:不包含结束值
for item in range(2,8,2):
    print(item)

# 写法2:
# range(开始,结束)
# 注意:间隔默认1
for item in range(2,8):
    print(item)

# 写法3:
# range(结束)
# 注意:开始默认0
for item in range(8):
    print(item)