from socket import *

sock = socket()
server_addr = ("127.0.0.1",8888)
sock.connect(server_addr)

# 收发数据
while True:
    msg = input(">>")
    sock.send(msg.encode()) # 字符串转换为字节串
    if msg == '##':
        break
    res = sock.recv(1024)
    print(res.decode())

# 关闭套接字
sock.close()








