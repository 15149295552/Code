"""
tcp多进程的并发网络模型
"""
from socket import *
from multiprocessing import Process

# 处理客户端请求
def handle(conn):
    while True:
        request = conn.recv(1024)
        if not request or request == b"##":
            break
        # .... 利用request做事情 .....
        print(request.decode())
        conn.send(b"OK")
    conn.close()

# 搭建基础网络模型
def main():
    # 创建监听套接字
    sock = socket()
    sock.bind(("0.0.0.0",8888))
    sock.listen()

    print("Listen the port 8888")
    # 循环建立连接关系
    while True:
        conn,addr = sock.accept()
        print("Connect from",addr)
        # 创建进程处理客户端事务
        p = Process(target=handle,args=(conn,))
        p.start()

if __name__ == '__main__':
    main()





