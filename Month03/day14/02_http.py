"""
http处理
"""
from socket import *

# 创建tcp套接字
sock = socket()
sock.bind(("0.0.0.0", 8000))
sock.listen()

while True:
    # 收到浏览器的连接
    conn,addr = sock.accept()
    print("Connect from", addr)
    # 接收http请求
    request = conn.recv(1024).decode()
    info = request.split(" ")[1] # 请求内容
    print(info)

    if info == '/':
        file = "html/demo02.html"
    else:
        file = "html/20221018.jpeg"

    response = b"HTTP/1.1 200 OK\r\n"
    response += b"Content-Type: text/html\r\n"
    response += b"\r\n"
    with open(file,'rb') as fr:
        response += fr.read()

    conn.send(response)  # 发送相应
    conn.close()

sock.close()
