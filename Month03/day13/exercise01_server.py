"""
练习： 任选一张照片，从客户端发送给服务端，在服务端
存储为 "20221018.jpeg",照片发送完成后客户端直接
结束。 服务端recv返回空则退出

客户端 ： 读取图片  发送图片内容
服务端 ： 接收图片内容  写入文件
"""
from socket import *

# 服务端 ： 接收图片内容  写入文件
def recv_image(conn):
    with open("20221018.jpeg",'wb') as fw:
        # 边接收边写入
        while True:
            data = conn.recv(1024)
            if data == b'##':
                break
            fw.write(data)

    conn.send("上传完毕".encode())

def main():
    # 创建监听套接字
    sock = socket()
    sock.bind(("0.0.0.0",8888))
    sock.listen()
    conn,addr = sock.accept() # 等待连接
    print("Connect from",addr)
    # 接收图片
    recv_image(conn)
    conn.close()
    sock.close()

main()


