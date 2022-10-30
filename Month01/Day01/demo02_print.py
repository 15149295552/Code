# print函数的使用介绍
# 适用性：显示数据

print(1, 2, 3)
print(1, 2, 3, 'python', 'Java')

# 参数： sep=' '  表示2个或2个以上数据的分隔方式
# print(1, 2, 3, sep='===')
# print('python', sep='+++')

# 参数： end='\n'  默认换行符，不换行：不设置为\n
# print('python 牛', end='-->')
# print('Java 牛')

# 说明：end 与 sep 设置顺序可以调换
print('java', 'python', end='', sep='+')