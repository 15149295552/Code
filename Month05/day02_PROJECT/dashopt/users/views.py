import jwt
import json
import time
import hashlib

from django.conf import settings
from django.core import mail
from django.http import JsonResponse
from users.models import UserProfile


def register_view(request):
    """
    注册功能视图逻辑
    1.获取请求体数据
    2.数据合法性校验
    3.确认用户名是否被占用
      3.1 被占用: 直接返回
      3.2 未被占用: 存入数据表
          生成token,返回响应
    """
    # 获取数据
    data = json.loads(request.body)
    username = data.get("uname")
    password = data.get("password")
    email = data.get("email")
    phone = data.get("phone")

    # 数据合法性校验
    if len(username) < 6 or len(username) > 11:
        return JsonResponse({"code": 10100, "error": "用户名不合法"})

    if len(password) < 6 or len(password) > 12:
        return JsonResponse({"code": 10101, "error": "密码不合法"})

    if len(phone) != 11:
        return JsonResponse({"code": 10102, "error": "手机号不合法"})

    # 是否被占用
    user_query = UserProfile.objects.filter(username=username)
    if user_query:
        # 被占用,直接返回
        return JsonResponse({"code": 10103, "error": "用户名已被占用"})

    # 可用,存入数据表
    try:
        user = UserProfile.objects.create(username=username, password=md5_string(password), email=email, phone=phone)
    except Exception as e:
        return JsonResponse({"code": 10104, "error": "该用户名已被占用"})

    # 发送激活邮件
    verify_url = f"http://127.0.0.1:7000/dadashop/templates/active.html?code={username}"
    send_active_email(email, verify_url)

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
    1.获取请求体数据(用户名和密码)
    2.校验用户名和密码
    3.签发token,返回响应
    """
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")

    try:
        user = UserProfile.objects.get(username=username)
    except Exception as e:
        print("查询异常:", e)
        return JsonResponse({"code": 10105, "error": "用户名或密码错误"})

    if user.password != md5_string(password):
        return JsonResponse({"code": 10106, "error": "用户名或密码错误"})

    token = make_token(username)
    # 返回响应
    result = {
        'code': 200,
        'username': username,
        'token': token,
        'carts_count': 0
    }

    return JsonResponse(result)


def active_view(request):
    """
    邮件激活视图逻辑
    1.一查二改三保存  is_active=True
    """
    pass


def md5_string(string):
    """
    功能函数:md5加密
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


def send_active_email(email, verify_url):
    """
    功能函数:发送激活邮件
    """
    subject = "达达商城激活邮件"
    message = f"欢迎注册达达商城,请点击激活链接进行激活:{verify_url}"

    mail.send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )














