"""
服务搭建，逻辑处理
1. 搭建网络服务 ： 并发网络模型
2. 处理http请求
3. 组织返回响应
"""
from socket import *
from threading import Thread
from dict_db import *


# http处理
class HTTPHandle(Thread):
    def __init__(self, conn, cli, html):
        self.conn = conn
        self.cli = cli
        self.html = html  # 网页存放位置
        self.db = Dict(user="root", password="123456", database="dict", charset="utf8")  # 用于数据库处理
        super().__init__(daemon=True)  # 分支线程随主线程结束

    # 释放资源
    def _close(self):
        self.db.close()
        self.conn.close()

    # 主体逻辑处理方法 (流程)
    def run(self):
        # 接收HTTP请求
        request = self.conn.recv(1024).decode()
        if not request:
            self._close()
            return
        # 解析请求
        parse = self._parse_request(request)
        print(f"{self.cli} : {parse}")
        # 处理请求 response : bytes
        response = self.do_request(parse)
        # 发送响应
        self.conn.send(response)
        self._close()

    # 处理请求  {method,info,body}
    def do_request(self, parse):
        path = parse["info"].split("?")[0]
        if path == "/register":
            response = self.do_register(parse['body'])
        elif path == "/login":
            response = self.do_login(parse['body'])
        elif path == "/search":
            response = self.do_search(parse["info"].split("?")[1])
        else:
            # 请求静态网页 /  /login.html
            response = self.get_html(path)
        return response

    # data --> # word=hello
    def do_search(self, data):
        word = data.split('=')[-1]  # 提取单词
        res = self.db.search(word)
        if res:
            mean = res[0]
        else:
            mean = "the word not found!"

        # 生成一个新的网页，伪装了原网页增加一个解释
        with open(self.html + "/search_res.html") as fr:
            html = fr.read()
        response = "HTTP 200 OK\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += html % (word, mean)
        return response.encode()

    # data登录请求的请求体user=admin&pwd1=abc123
    def do_login(self, data):
        # 提取用户名密码
        tmp = data.split("&")
        user = tmp[0].split('=')[-1]
        pwd = tmp[1].split('=')[-1]
        # 数据库处理函数  成功-》search  失败-》登录
        if self.db.login(user, pwd):
            return self.get_html("/search.html")
        return self.get_html("/login.html")

    # data注册请求的请求体user=admin&pwd1=abc123&pwd2=abc123
    def do_register(self, data):
        # 提取用户名密码
        tmp = data.split("&")
        user = tmp[0].split('=')[-1]
        pwd = tmp[1].split('=')[-1]
        # 数据库处理函数  成功-》login  失败-》注册
        if self.db.register(user, pwd):
            return self.get_html("/login.html")
        return self.get_html("/register.html")

    # 提供静态网页或者图片
    def get_html(self, path):
        if path == '/':
            path = "/login.html"  # 主页默认为登录页

        response = b"HTTP 200 OK\r\n"
        if path[-3:] == "css":
            response += b"Content-Type:text/css\r\n"
        else:
            response += b"Content-Type:text/html\r\n"
        response += b"\r\n"
        try:
            with open(self.html + path, 'rb') as fr:
                response += fr.read()
        except:
            with open(self.html + "/404.html", 'rb') as fr:
                response += fr.read()
        return response

    # 请求解析
    def _parse_request(self, request):
        lines = request.split("\n")  # 按照行
        tmp = lines[0].split(' ')
        parse = {"method": tmp[0], "info": tmp[1]}
        if tmp[0] == 'POST':
            parse["body"] = lines[-1]
        return parse  # 请求类型 请求内容 请求体


# 多线程并发网络服务
class DictServer:
    def __init__(self, host="", port=0, **kwargs):
        self.host = host
        self.port = port
        self.kwargs = kwargs
        self.address = (host, port)
        self.sock = self._create_socket()

    def _create_socket(self):
        sock = socket()
        sock.bind(self.address)
        return sock

    def serve_forever(self):
        self.sock.listen()
        print(f"------Listen the port {self.port}------")
        # 循环接收客户端的连接
        while True:
            try:
                conn, addr = self.sock.accept()
            except KeyboardInterrupt:
                self.sock.close()
                return
            # 为连接的客户端创建线程
            t = HTTPHandle(conn, addr, **self.kwargs)
            t.start()


if __name__ == '__main__':
    dict = DictServer(host="0.0.0.0", port=8000, html="./static")
    dict.serve_forever()
