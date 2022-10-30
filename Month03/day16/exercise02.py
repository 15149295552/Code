"""
1. 搭建一个并发网络模型
2. 处理HTTP请求
   解析请求   组织数据  发送响应
"""
from socket import *
from threading import Thread

# 处理浏览器HTTP请求
class Handle(Thread):
    def __init__(self, conn, html):
        self.conn = conn
        self.html = html # 网页存放位置
        super().__init__()

    # 处理http请求 只有GET
    def run(self):
        # 接收http请求
        request = self.conn.recv(1024).decode()
        if not request:
            self.conn.close()
            return
        # 解析请求  请求内容
        info = request.split(' ')[1]
        print("请求:",info)

        # 如果请求主页做特殊处理
        if info == "/":
            info = "/index.html"
        response = self._response(info)
        self.conn.send(response)
        self.conn.close()


    # 组织响应
    def _response(self,file):
        response = b"HTTP/1.1 200 OK\r\n"
        response += b"Content-Type: text/html\r\n"
        response += b"\r\n"
        try:
            with open(self.html + file, 'rb') as fr:
                response += fr.read()
        except:
            # 文件打开失败说明可能不存在
            with open(self.html + "/404.html", 'rb') as fr:
                response += fr.read()
        return response


# 多线程并发网络模型
class TCPThreadServer:
    def __init__(self, host="0.0.0.0", port=0, **kwargs):
        self.host = host
        self.port = port
        self._kwargs = kwargs
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
    httpd = TCPThreadServer(host="0.0.0.0", port=8000,html="./static")
    httpd.main()  # 服务启动
