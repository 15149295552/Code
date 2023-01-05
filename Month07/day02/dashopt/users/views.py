import hashlib
import json
import time
import jwt

from django.conf import settings
from django.http import JsonResponse
from django.views import View
from users.models import UserProfile

from utils.logging_dec import logging_check


def register_view(request):
    """
    注册功能视图逻辑
    1.获取请求体数据(用户名、密码、邮箱、手机号)
    2.数据合法性校验
      用户名6-11位,密码6-12位,手机号11位
    3.判断用户名是否被占用
      3.1 被占用,直接返回
      3.2 未被占用,存入用户表,生成token,返回响应(API文档)
    """
    # 获取请求体数据
    data = json.loads(request.body)
    username = data.get("uname")
    password = data.get("password")
    phone = data.get("phone")
    email = data.get("email")
    verify = data.get("verify")

    # 数据合法性校验
    if len(username) < 6 or len(username) > 11:
        return JsonResponse({"code": 10100, "error": "用户名不合法"})

    if len(password) < 6 or len(password) > 12:
        return JsonResponse({"code": 10101, "error": "密码不合法"})

    if len(phone) != 11:
        return JsonResponse({"code": 10102, "error": "手机号不合法"})

    # 用户名是否被占用
    user_query = UserProfile.objects.filter(username=username)
    if user_query:
        return JsonResponse({"code": 10103, "error": "用户名被占用"})

    # 存入数据表
    pwd_md5 = md5_func(password)
    user = UserProfile.objects.create(username=username, password=pwd_md5, email=email, phone=phone)

    token = make_token(username)
    # 返回响应
    result = {
        'code': 200,
        'username': username,
        'token': token,
        'carts_count': 0
    }

    return JsonResponse(result)


def login_view(request):
    """
    登录功能视图逻辑
    1.获取请求体数据
    2.校验用户名和密码
      2.1 用户名或密码错误: 直接return
      2.2 正确,生成token,返回响应(API文档)
    """
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")

    try:
        user = UserProfile.objects.get(username=username)
    except Exception as e:
        return JsonResponse({"code": 10104, "error": "用户名错误"})

    if user.password != md5_func(password):
        return JsonResponse({"code": 10105, "error": "用户名或密码错误"})

    token = make_token(username)
    # 返回响应
    result = {
        'code': 200,
        'username': username,
        'token': token,
        'carts_count': 0
    }

    return JsonResponse(result)


class AddressView(View):
    @logging_check
    def get(self, request, username):
        return JsonResponse({"code": 200})

    @logging_check
    def post(self, request, username):
        pass

    @logging_check
    def put(self, request, username):
        pass

    @logging_check
    def delete(self, request, username):
        pass


def md5_func(string):
    """
    功能函数: md5加密函数
    """
    m = hashlib.md5()
    m.update(string.encode())

    return m.hexdigest()


def make_token(username, expire=86400):
    """
    功能函数: 生成token
    """
    payload = {
        "exp": int(time.time()) + expire,
        "username": username
    }
    key = settings.JWT_TOKEN_KEY

    return jwt.encode(payload, key, algorithm="HS256")







