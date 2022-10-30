"""
tcp客户端基本流程
"""
from socket import *

# 创建tcp套接字 默认值就是 ipv4 tcp
sock = socket()

# 连接服务端
server_addr = ("127.0.0.1",8888)
sock.connect(server_addr)

# 收发数据
while True:
    msg = input(">>")
    sock.send(msg.encode()) # 字符串转换为字节串
    if msg == '##':
        break # 结束循环
    res = sock.recv(1024)
    print(res.decode())


# 关闭套接字
sock.close()








