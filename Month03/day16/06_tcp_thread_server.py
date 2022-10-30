"""
多线程网络并发
"""
from socket import *
from threading import Thread

# 实现具体任务
class Handle(Thread):
    def __init__(self, conn, value):
        self.conn = conn
        self.value = value
        super().__init__()

    def run(self):
        print(self.value)
        while True:
            request = self.conn.recv(1024)
            if not request or request == b"##":
                break
            # .... 利用request做事情 .....
            print(request.decode())
            self.conn.send(b"OK")
        self.conn.close()


class TCPThreadServer:
    def __init__(self, host="0.0.0.0", port=0, **kwargs):
        self.host = host
        self.port = port
        self._kwargs = kwargs  # {"value":"....."}
        self.address = (host, port)
        self._sock = self._create_socket()

    def _create_socket(self):
        sock = socket()
        sock.bind(self.address)
        return sock

    # 启动服务
    def main(self):
        self._sock.listen()
        print("Listen the port %d" % self.port)
        # 循环接收连接
        while True:
            conn, addr = self._sock.accept()
            print(f"------- connect {addr} -------")
            # 使用自定义线程类创建线程
            t = Handle(conn, **self._kwargs)
            t.start()


if __name__ == '__main__':
    serve = TCPThreadServer(host="0.0.0.0", port=8888, value="客户端和你要交互啦！")
    serve.main()  # 服务启动
