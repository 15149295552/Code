"""
练习：自己编写一个服务端程序，通过浏览器访问服务端
如果在地址栏输入 127.0.0.1:8000 则能够获取到一个
注册页面。在该页面输入用户名密码，提交给服务端的换
则能够得到一个登录成功的提示，并且该用户密码会存储到
数据库的 user 表里
（user 表提前建好 ： id   user  password ）

create table user (
id int primary key auto_increment,
user char(30) unique,
password char(64)
);
"""
from socket import *
import pymysql

# 插入数据库
def save(user,password):
    sql = "insert into user (user,password) values (%s,%s);"
    try:
        cur.execute(sql,[user,password])
        db.commit()
        return True
    except:
        db.rollback()


def do_post(conn,info):
    # 提取用户名密码 user=yourname&pwd=yourpwd
    tmp = info.split("&")
    user = tmp[0].split("=")[-1]
    password = tmp[1].split("=")[-1]
    # print(user,password)
    # 存入数据库
    if save(user,password):
        do_get(conn, file="html/success.html")
    else:
        do_get(conn, file="html/fail.html")

# 处理get请求
def do_get(conn,file="demo.html"):
    response = b"HTTP/1.1 200 OK\r\n"
    response += b"Content-Type: text/html\r\n"
    response += b"\r\n"
    with open(file, 'rb') as fr:
        response += fr.read()
    conn.send(response)  # 发送相应

def handle(conn):
    # 获取http请求
    request = conn.recv(1024).decode()
    if not request:
        return
    lines = request.split("\n")
    method = lines[0].split(' ')[0] # 获取请求类型
    # 分类讨论
    if method == 'GET':
        do_get(conn)
    else:
        # lines[-1] -> user=yourname&pwd=yourpwd
        do_post(conn,lines[-1])

# 处理http请求
def web_server():
    # 创建tcp套接字
    sock = socket()
    sock.bind(("0.0.0.0", 8000))
    sock.listen()
    while True:
        # 收到浏览器的连接
        conn, addr = sock.accept()
        print("Connect from", addr)
        # 处理http请求
        handle(conn)
        conn.close()

if __name__ == '__main__':
    db = pymysql.connect(user="root", password="123456", database="dict", charset="utf8")
    cur = db.cursor()
    web_server()






