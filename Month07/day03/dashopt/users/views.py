import jwt
import json
import time
import hashlib

from django.core import mail
from django.views import View
from django.conf import settings
from django.db import transaction
from django.http import JsonResponse
from users.models import UserProfile, Address

from utils.logging_dec import logging_check
from utils.baseview import BaseView


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

    # 发送激活邮件
    verify_url = "http://127.0.0.1:7000/dadashop/templates/active.html"
    send_active_email(email, username, verify_url)

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


class AddressView(BaseView):
    # @logging_check
    def get(self, request, username):
        """
        查询收货地址视图逻辑
        {"code":200, "addresslist": [{},{},...]}
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

    # @logging_check
    def post(self, request, username):
        """
        新增地址视图逻辑
        1.获取请求体数据
        2.存入数据表(Address)
          2.1 是第一个地址: 新增并设置为默认
          2.2 非第一个地址: 新增为非默认地址
        3.返回响应(API文档)
        """
        # 获取请求体数据
        data = json.loads(request.body)
        receiver = data.get("receiver")
        receiver_phone = data.get("receiver_phone")
        address = data.get("address")
        postcode = data.get("postcode")
        tag = data.get("tag")

        # 确认是否为第一个地址
        user = request.myuser
        addr_query = Address.objects.filter(user_profile=user, is_delete=False)
        is_default = False if addr_query else True

        # 存入地址表
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

    # @logging_check
    def put(self, request, username, id):
        """
        修改地址视图逻辑
        1.获取请求体数据
        2.一查二改三保存
        3.返回响应(API文档)
        """
        data = json.loads(request.body)
        receiver = data.get("receiver")
        receiver_mobile = data.get("receiver_mobile")
        address = data.get("address")
        tag = data.get("tag")
        user = request.myuser

        try:
            addr = Address.objects.get(user_profile=user, id=id, is_delete=False)
        except Exception as e:
            return JsonResponse({"code": 10107, "error": "该地址不存在!"})

        addr.receiver = receiver
        addr.receiver_mobile = receiver_mobile
        addr.address = address
        addr.tag = tag
        addr.save()

        return JsonResponse({"code": 200, "data": "地址修改成功!"})

    # @logging_check
    def delete(self, request, username, id):
        """
        删除地址视图逻辑(伪删除)
        一查二改三保存操作(is_delete=True)
        """
        # 一查
        user = request.myuser
        try:
            addr = Address.objects.get(user_profile=user, id=id, is_delete=False)
        except Exception as e:
            return JsonResponse({"code": 10106, "error": "该地址不存在"})

        # 二改三保存
        addr.is_delete = True
        addr.save()

        return JsonResponse({"code": 200, "data": "删除地址成功!"})


class DefaultAddressView(BaseView):
    # @logging_check
    def post(self, request, username):
        """
        设置默认地址视图逻辑
        1.获取请求体数据(id)
        2.两个ORM更新操作
          2.1 把原来默认地址取消默认
          2.2 把现在地址设置为默认
        3.返回响应
        """
        data = json.loads(request.body)
        addr_id = data.get("id")
        user = request.myuser

        # 开启事务
        with transaction.atomic():
            # 创建存储点
            sid = transaction.savepoint()
            try:
                # 原来默认地址取消默认
                old_query = Address.objects.filter(user_profile=user, is_default=True, is_delete=False)
                # old_query: <QuerySet [<xxx>]>
                if old_query:
                    old_user = old_query[0]
                    old_user.is_default = False
                    old_user.save()

                # 现地址设置为默认
                now_user = Address.objects.get(id=addr_id, user_profile=user, is_delete=False)
                now_user.is_default = True
                now_user.save()
            except Exception as e:
                # 回滚 + 返回
                transaction.savepoint_rollback(sid)
                return JsonResponse({"code": 10108, "error": "设置默认失败"})

            # 提交事务
            transaction.savepoint_commit(sid)

        # 返回响应
        return JsonResponse({"code": 200, "data": "设置默认地址成功!"})


def active_view(request):
    """
    邮件激活视图逻辑
    把某个用户的is_active=True
    """
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


def send_active_email(email, username, verify_url):
    """
    功能函数: 发送邮件
    """
    subject = "达达商城激活邮件"
    message = f"""
    欢迎您:{username},请点击激活链接进行激活:<a href="{verify_url}" target="_blank">点击此处</a>"""

    mail.send_mail(
        subject=subject,
        # message: 发送文本内容邮件
        message="",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        # html_message: 发送html格式邮件
        html_message=message
    )





