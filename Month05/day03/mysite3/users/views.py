import hashlib

from django.shortcuts import render
from django.http import HttpResponse
from users.models import UserProfile


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