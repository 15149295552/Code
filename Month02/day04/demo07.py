"""
    切片
        定位多个元素
"""
message = "我是花果山水帘洞美猴王孙悟空"
# 写法1:
# 容器名[开始:结束:间隔]
# 注意：不包含结束
print(message[1:5:2])
# 写法2:
# 容器名[开始:结束]
# 注意：间隔默认为1
print(message[1:5])
# 写法3:
# 容器名[:结束]
# 注意：开始默认为头
print(message[:5])
# 写法4:
# 容器名[:]
# 注意：开始默认为头
print(message[:])
print(message[-3:])

message = "我是花果山水帘洞美猴王孙悟空"
print(message[2:5])
# 是花果山水帘洞美猴王孙悟
print(message[1:-1])
# 花果山水帘洞美猴王孙
print(message[2:-2])
# 山水帘洞美猴王
print(message[4:-3]) #
print(message[4:1]) # 不报错,但没元素
print(message[4:1:-1]) #
print(message[::-1]) # 倒序





