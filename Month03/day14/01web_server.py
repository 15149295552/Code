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
    request = conn.recv(1024)
    print(request.decode())

    # 按照http格式组织相应
    # response = "HTTP/1.1 200 OK\r\n"
    # response += "Content-Type: text/html\r\n"
    # response += "\r\n"
    # response += "<h1>Hello world</h1>"

    # 二进制数据的处理
    response = b"HTTP/1.1 200 OK\r\n"
    response += b"Content-Type: image/jpeg\r\n"
    response += b"\r\n"
    with open("html/20221018.jpeg", 'rb') as fr:
        response += fr.read()
    conn.send(response)  # 发送相应

    conn.close()

sock.close()
