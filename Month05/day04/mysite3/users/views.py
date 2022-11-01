import hashlib

from django.shortcuts import render
from django.http import HttpResponse
from users.models import UserProfile


def md5_string(string):
    """功能函数:md5加密"""
    m = hashlib.md5()
    m.update(string.encode())

    return m.hexdigest()


def register_view(request):
    if request.method == "GET":
        return render(request, "users_register.html")
    elif request.method == "POST":
        # 执行注册逻辑
        # 1.获取请求体数据
        # 2.判断两次密码是否一致
        # 3.判断用户名是否被占用
        # 4.将数据存入用户表
        data = request.POST
        username = data.get("username")
        password = data.get("password")
        password_again = data.get("password_again")
        email = data.get("email")
        mobile = data.get("mobile")

        if password != password_again:
            return HttpResponse("两次密码不一致")

        # 判断用户名是否被占用
        user_query = UserProfile.objects.filter(username=username)
        if user_query:
            return HttpResponse("该用户名已被占用")

        # 密码加密
        m = hashlib.md5()
        m.update(password.encode())
        pwd_md5 = m.hexdigest()

        # 存入数据表
        UserProfile.objects.create(username=username, password=pwd_md5, email=email, mobile=mobile)

        return HttpResponse("恭喜,注册成功!")
    else:
        return HttpResponse("违法请求")


def login_view(request):
    if request.method == "GET":
        return render(request, "users_login.html")
    elif request.method == "POST":
        # 登录逻辑
        # 1.获取请求体数据
        # 2.和数据库中数据比对
        data = request.POST
        username = data.get("username")
        password = data.get("password")

        user_query = UserProfile.objects.filter(username=username)

        if not user_query:
            return HttpResponse("用户名错误")

        # user_query: [<UserProfile object>]
        user = user_query[0]

        m = hashlib.md5()
        m.update(password.encode())
        password = m.hexdigest()

        if password != user.password:
            return HttpResponse("用户名或密码错误")

        return HttpResponse("登录成功")
    else:
        return HttpResponse("违法请求")


def login_get_view(request):
    if request.method == "GET":
        return render(request, "users_login.html")
    elif request.method == "POST":
        # 登录逻辑
        # 1.获取请求体数据
        # 2.和数据库中数据比对
        data = request.POST
        username = data.get("username")
        password = data.get("password")

        try:
            user = UserProfile.objects.get(username=username)
        except Exception as e:
            # 用户名错误
            return HttpResponse("用户名错误")

        m = hashlib.md5()
        m.update(password.encode())
        password = m.hexdigest()

        if password != user.password:
            return HttpResponse("用户名或密码错误")

        return HttpResponse("登录成功")
    else:
        return HttpResponse("违法请求")


def update_view(request):
    """
    修改密码视图逻辑
    """
    if request.method == "GET":
        # 返回页面
        return render(request, "users_update.html")
    elif request.method == "POST":
        # 修改密码(一查二改三保存)
        data = request.POST
        username = data.get("username")
        password = data.get("password")
        new_password = data.get("new_password")
        new_password2 = data.get("new_password2")

        # 校验用户名和密码
        try:
            user = UserProfile.objects.get(username=username)
        except Exception as e:
            return HttpResponse("用户名错误")

        if user.password != md5_string(password):
            return HttpResponse("用户名或密码错误")

        if new_password != new_password2:
            return HttpResponse("两次密码不一致")

        # 一查二改三保存
        user.password = md5_string(new_password)
        user.save()
        return HttpResponse("密码更改成功")
    else:
        return HttpResponse("违法请求")


def delete_view(request):
    """
    http://127.0.0.1:8000/v1/users/delete_user?username=dilireba&password=123456
    注销用户视图逻辑
    1.获取用户名和密码数据
    2.校验
    3.删除用户(一查二删除)
    """
    data = request.GET
    username = data.get("username")
    password = data.get("password")

    user_query = UserProfile.objects.filter(username=username)
    if not user_query:
        return HttpResponse("用户名错误")

    user = user_query[0]
    if user.password != md5_string(password):
        return HttpResponse("用户名或密码错误")

    # 删除
    user.delete()

    return HttpResponse("注销成功")




# # 增
# user = UserProfile.objects.create(username="zhaoliying", password="123456", email="309435365@qq.com", mobile="13603263409")
# print("----->", user)
# print("----->", user.username)
# print("----->", user.password)

# # 查询
# result1 = UserProfile.objects.filter(username="zhaoliying")
# result2 = UserProfile.objects.filter(username="dilireba")
# print("result1---->", result1)
# print("result2---->", result2)