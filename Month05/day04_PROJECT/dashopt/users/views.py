import jwt
import json
import time
import base64
import random
import hashlib

from django.conf import settings
from django.core import mail
from django.core.cache import caches
from django.http import JsonResponse
from django.views import View
from django.db import transaction
from users.models import UserProfile, Address

from utils.logging_dec import logging_check
from utils.smsapi import send_message

EMAIL_CACHE = caches["default"]
SMS_CACHE = caches["sms"]


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
    # 获取短信验证码
    verify = data.get("verify")

    key = f"sms_{phone}"
    redis_code = SMS_CACHE.get(key)

    if not redis_code:
        return JsonResponse({"code": 10114, "error": "验证码已过期,请重新获取"})

    if verify != str(redis_code):
        return JsonResponse({"code": 10115, "error": "验证码错误,请重新输入"})

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
    # base64("1016_liying")
    code_num = random.randint(1000, 9999)
    code_str = f"{code_num}_{username}"
    code = base64.urlsafe_b64encode(code_str.encode()).decode()

    verify_url = f"http://127.0.0.1:7000/dadashop/templates/active.html?code={code}"
    send_active_email(email, verify_url)

    # 存入redis: {"email_liying": 1111}
    key = f"email_{username}"
    EMAIL_CACHE.set(key, code_num, 86400 * 3)

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
    1.获取查询字符串code
    2.校验随机数
    3.一查二改三保存  is_active=True
    4.返回响应
    """
    # code: Mjk1MF9kYXRhYmFzZQ==
    code = request.GET.get("code")
    # code_str: 1016_liying
    code_str = base64.urlsafe_b64decode(code.encode()).decode()
    code_num, username = code_str.split("_")
    key = f"email_{username}"
    redis_num = EMAIL_CACHE.get(key)

    if not redis_num:
        return JsonResponse({"code": 10107, "error": "激活链接已过期"})

    if code_num != str(redis_num):
        return JsonResponse({"code": 10108, "error": "激活失败!"})

    # 一查二改三保存
    try:
        user = UserProfile.objects.get(username=username)
    except Exception as e:
        return JsonResponse({"code": 10109, "error": "激活失败,再试一次~"})

    user.is_active = True
    user.save()

    return JsonResponse({"code": 200, "data": "激活成功!"})


class AddressView(View):
    @logging_check
    def get(self, request, username):
        """
        查询地址视图逻辑
        {"code":200,"addresslist":[{},]}
        """
        user = request.myuser
        addr_query = Address.objects.filter(user_profile=user, is_delete=False)
        addresslist = []
        for addr in addr_query:
            addr_dict = {
                'id': addr.id,
                'address': addr.address,
                'receiver': addr.receiver,
                'receiver_mobile': addr.receiver_mobile,
                'tag': addr.tag,
                'postcode': addr.postcode,
                'is_default': addr.is_default,
            }
            addresslist.append(addr_dict)

        return JsonResponse({"code": 200, "addresslist": addresslist})

    @logging_check
    def post(self, request, username):
        """
        新增地址视图逻辑
        1.获取请求体数据
        2.存入Address表
          2.1 第一个地址: 设置为默认
          2.2 非第一个地址: 非默认地址
        3.返回响应
        """
        data = json.loads(request.body)
        receiver = data.get("receiver")
        receiver_phone = data.get("receiver_phone")
        address = data.get("address")
        postcode = data.get("postcode")
        tag = data.get("tag")

        user = request.myuser
        addr_query = Address.objects.filter(user_profile=user, is_delete=False)

        is_default = False if addr_query else True

        Address.objects.create(
            user_profile=user,
            receiver=receiver,
            address=address,
            postcode=postcode,
            receiver_mobile=receiver_phone,
            tag=tag,
            is_default=is_default,
        )

        return JsonResponse({"code": 200, "data": "新增地址成功"})

    @logging_check
    def put(self, request, username, id):
        """
        修改地址视图逻辑
        1.获取请求体数据
        2.一查二改三保存
        3.返回响应
        """
        data = request.mydata
        receiver = data.get("receiver")
        receiver_mobile = data.get("receiver_mobile")
        address = data.get("address")
        tag = data.get("tag")

        # ORM更新
        try:
            addr = Address.objects.get(id=id, user_profile=request.myuser, is_delete=False)
        except Exception as e:
            return JsonResponse({"code": 10110, "error": "没有该地址!"})

        addr.receiver = receiver
        addr.receiver_mobile = receiver_mobile
        addr.address = address
        addr.tag = tag
        addr.save()

        return JsonResponse({"code": 200, "data": "修改地址成功!"})

    @logging_check
    def delete(self, request, username, id):
        """
        删除地址视图逻辑
        一查二改三保存
        """
        try:
            addr = Address.objects.get(id=id, is_delete=False, user_profile=request.myuser)
        except Exception as e:
            return JsonResponse({"code": 10111, "error": "该地址异常!"})

        addr.is_delete = True
        addr.save()

        return JsonResponse({"code": 200, "data": "删除地址成功!"})


class DefaultAddressView(View):
    @logging_check
    def post(self, request, username):
        """
        设置默认视图逻辑
        1.获取请求体数据(id)
        2.两个orm操作
          2.1 将原来默认地址取消默认
          2.2 将现地址设置为默认
        3.返回响应
        """
        addr_id = request.mydata.get("id")
        user = request.myuser

        # 开启事务
        with transaction.atomic():
            # 创建存储点
            sid = transaction.savepoint()
            # 两个orm操作
            try:
                old_query = Address.objects.filter(is_default=True, user_profile=user, is_delete=False)
                if old_query:
                    old_default = old_query[0]
                    old_default.is_default = False
                    old_default.save()

                new_default = Address.objects.get(id=addr_id, user_profile=user, is_delete=False)
                new_default.is_default = True
                new_default.save()
            except Exception as e:
                print("设置默认异常:", e)
                # 回滚
                transaction.savepoint_rollback(sid)
                return JsonResponse({"code": 10112, "error": "设置默认失败"})

            # 提交事务
            transaction.savepoint_commit(sid)

        return JsonResponse({"code": 200, "data": "设置默认成功!"})


def sms_view(request):
    """
    发送短信验证码视图逻辑
    1.获取请求体数据
    2.调用接口发送短信
    3.存入redis,设置有效期
    4.返回响应
    """
    data = json.loads(request.body)
    phone = data.get("phone")

    # 确认:1分钟之内是否发送过
    key_expire = f"expire_{phone}"
    code = SMS_CACHE.get(key_expire)
    if code:
        return JsonResponse({"code": 10113, "error": "短信发送过于频繁"})

    code_num = random.randint(100000, 999999)
    datas = (code_num, 5)
    send_message("1", phone, datas)

    # 存入Redis数据库:用于后期校验
    # {"sms_13603263409": 871016}
    key = f"sms_{phone}"
    SMS_CACHE.set(key, code_num, 300)

    # 存入Redis数据库:用于控制频率
    SMS_CACHE.set(key_expire, code_num, 60)

    return JsonResponse({"code": 200, "data": "短信发送成功!"})


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














