# 字符串： content = "我是京师监狱狱长金海。"
content = "我是京师监狱狱长金海。"

# 打印第一个字符、最后一个字符、中间字符
print('第一个字符', content[0])
print('最后一个字', content[-1])
print('中间字符', content[5], content[len(content)//2])

# 打印字前三个符、打印后三个字符
print('前3个字符', content[:3])
print('后3个字符', content[-3:])

# 命题：金海在字符串content中
print('金海' in content)

# 命题：京师监狱不在字符串content中
print('京师监狱' not in content)

# 通过切片打印“京师监狱狱长”
print('京师监狱狱长', content[2:-3])

# 通过切片打印“长狱狱监师京”
print('长狱狱监师京', content[-4:1:-1])
print('长狱狱监师京', content[2:-3][::-1])

# 通过切片打印“我师狱海”
print('我师狱海', content[::3])

# 倒序打印字符
print('倒序打印字符', content[::-1])