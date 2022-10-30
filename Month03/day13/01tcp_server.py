"""
tcp服务端标准化流程   重点代码
"""
from socket import *

# 创建tcp套接字
sock = socket(AF_INET,SOCK_STREAM)

# 绑定地址
sock.bind(("0.0.0.0",8888))

# 设置监听
sock.listen()

# 阻塞等待处理客户端连接
while True:
    print("等待客户端连接...")
    conn,addr = sock.accept()
    print("连接了",addr)

    # 数据收发  必须使用字节串数据
    while True:
        data = conn.recv(5)
        # 如果返回空字节串  收到了特殊的标志##
        if not data or data == b"##":
            break
        print("收到:",data.decode())
        conn.send(b'Thanks')  # 发送字节串

    conn.close()

# 关闭连接
sock.close()







