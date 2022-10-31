"""
mysql -uroot -p123456

create database aiddb default charset utf8;
use aiddb;
create table user_tab(
id int primary key auto_increment,
username varchar(20),
password char(32)
);
insert into user_tab(username,password) values("zhaoliying", "123456"),("reba","123456");
"""

import pymysql
from django.http import HttpResponse


def login_view(request):
    """
    登录视图逻辑
    # GET请求:http://127.0.0.1:8000/v1/users/login?username=zhaoliying&password=123456
    """
    # 1.先获取提交过来的用户名和密码
    username = request.GET.get("username")
    password = request.GET.get("password")

    # 2.获取数据库中的用户名和密码，比较
    db = pymysql.connect(host="localhost", user="root", password="123456", database="aiddb", charset="utf8")
    cur = db.cursor()
    cur.execute("select username,password from user_tab where username=%s", [username])

    # userinfo: ("liying","123456")  | None
    userinfo = cur.fetchone()
    if not userinfo:
        return HttpResponse("用户名或密码错误")

    if userinfo[1] != password:
        return HttpResponse("-用户名或密码错误")

    return HttpResponse("恭喜你,登录成功!")











