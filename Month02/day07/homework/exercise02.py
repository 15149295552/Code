"""
    将列表中的数字累减
        list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
    结果：806400
"""
list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
result = list02[0]
for i in range(1, len(list02)):
    result -= list02[i]
print(result)

# 不包含结束值
# range(结束)
# range(开始,结束)
# range(开始,结束,间隔)
list01 = [1,2]
# len(列表) 返回列表长度2
# range(len(列表)) 返回 0 1
# list01[len(list01)] 会报错