"""
练习1 客户端
"""
from socket import *
from time import sleep

# 客户端 ： 读取图片  发送图片内容
def send_image(sock):
    with open("1.jpeg",'rb') as fr:
        # 边读取，边发送
        while True:
            data = fr.read(1024)
            if not data:
                break
            sock.send(data)
    sleep(0.1) # 防止粘包
    sock.send(b"##") # 让服务端结束循环的方法
    print(sock.recv(1024).decode())


def main():
    sock = socket()
    sock.connect(("127.0.0.1",8888))
    send_image(sock)
    sock.close()

main()