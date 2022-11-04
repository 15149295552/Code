import base64
import time
from django.core import mail
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page


def set_cookie_view(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        # 1.获取用户名和密码
        # 2.校验用户名和密码
        #   2.1 错误: 返回 用户名或密码错误
        #   2.2 正确: 设置cookie，返回登录成功
        username = request.POST.get("username")
        password = request.POST.get("password")
        # 假如数据库用户信息: zhaoliying 123456
        if username != "zhaoliying" or password != "123456":
            # 登录失败,不设置cookie!
            return HttpResponse("用户名或密码错误")

        # 登录成功
        resp = HttpResponse("登录成功!")

        # 设置cookie: 携带用户标识
        username = base64.b64encode(b"zhaoliying").decode()
        resp.set_cookie("username", username, 300)

        return resp


def get_cookie_view(request):
    """查看订单视图逻辑"""
    # 1.获取cookie(当初存储在cookie的用户标识)
    # 2.base64解码
    # 3.执行查询订单的逻辑
    # 4.返回订单数据
    # username: slfkjaselfjaes==
    username = request.COOKIES.get("username")
    username = base64.b64decode(username.encode()).decode()

    # 查询订单数据
    return HttpResponse(f"{username}:给你订单数据,噢耶!")


def set_session_view(request):
    """
    假如在登录
    """
    # 1.校验用户名密码信息
    # 2.用户信息没问题,设置session(存放用户标识)

    request.session["username"] = "zhaoliying"

    return HttpResponse("登录成功!设置session成功!")


def get_session_view(request):
    username = request.session.get("username")
    # 其他业务逻辑(查询该用户订单、查询该用户的微博...)

    return HttpResponse(f"{username}: 成功")


# @cache_page(30)
def test_cache_view(request):
    print("わたしはあなたを爱する")

    return HttpResponse(time.time())


def test_view(request):

    return HttpResponse("访问次数未超过5次~~")


def email_view(request):
    mail.send_mail(
        subject="将进酒-李白",
        message="君不见黄河之水天上来,奔流到海不复回",
        from_email="309435365@qq.com",
        recipient_list=["309435365@qq.com"]
    )

    return HttpResponse("恭喜你,邮件发送成功!")

