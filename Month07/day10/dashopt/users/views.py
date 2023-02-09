import base64
import random
import jwt
import json
import time
import hashlib
import requests

from django.core import mail
from django.views import View
from django.conf import settings
from django.db import transaction
from django.core.cache import caches
from django.http import JsonResponse

from carts.views import CartsView
from users.models import UserProfile, Address, WeiBoProfile

from utils.logging_dec import logging_check
from utils.baseview import BaseView
from utils.smsapi import send_message
from utils.smsapi_myself import SmsSDK
from .tasks import async_send_active_email, async_send_message


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
    # 短信验证码
    verify = data.get("verify")

    # 短信验证码校验
    key_expire = f"sms_{phone}_verify"
    redis_num = caches["sms_code"].get(key_expire)

    if not redis_num:
        # 过期
        return JsonResponse({"code": 10114, "error": "验证码过期,请重新获取"})

    if verify != str(redis_num):
        # 验证码错误
        return JsonResponse({"code": 10115, "error": "验证码错误,请重新输入"})

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

    # celery异步发送激活邮件
    # code: base64("1016_liying")
    verify_url = get_verify_url(username)
    # send_active_email(email, username, verify_url)
    async_send_active_email.delay(email, username, verify_url)

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

    carts_count = len(CartsView().get_carts_dict(user.id))
    # 返回响应
    result = {
        'code': 200,
        'username': username,
        'token': token,
        'carts_count': carts_count
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
    1.获取code
    2.校验用户合法性(随机数)
    3.把该用户的is_active=True(一查二改三保存)
    4.返回响应
    """
    # code: NzE5OV9saXlpbmc=
    code = request.GET.get("code")
    # code_str: 1016_zhaoliying
    code_str = base64.b64decode(code.encode()).decode()
    user_num, username = code_str.split("_")
    key = f"active_{username}"
    redis_num = caches["default"].get(key)
    if not redis_num:
        return JsonResponse({"code": 10109, "error": "激活失败"})

    if user_num != str(redis_num):
        return JsonResponse({"code": 10110, "error": "激活码错误"})

    # 激活用户(一查二改三保存)
    try:
        user = UserProfile.objects.get(username=username, is_active=False)
    except Exception as e:
        return JsonResponse({"code": 10111, "error": "该用户不存在!"})

    user.is_active = True
    user.save()

    # 清除激活数据,释放内存
    caches["default"].delete(key)

    return JsonResponse({"code": 200, "data": "激活成功!"})


def sms_view(request):
    """
    发送短信验证码视图逻辑
    1.获取请求体数据(手机号)
    2.发送短信
    3.返回响应
    {"sms_13603263409": 871016}
    """
    data = json.loads(request.body)
    phone = data.get("phone")
    # 判断1分钟之内是否发过
    key = f"sms_{phone}"
    redis_num = caches["sms_code"].get(key)
    if redis_num:
        return JsonResponse({"code": 10113, "error": "短信发送过于频繁"})

    code_num = random.randint(100000, 999999)
    datas = (code_num, 5)
    # 1.容联云接口
    # send_message("1", phone, datas)
    # celery异步发送短信
    async_send_message.delay(phone, datas)

    # 2.自己短信接口
    # sdk = SmsSDK(settings.ACCID, settings.ACCTOKEN, settings.APPID)
    # sdk.sendMessage("1", phone, datas)

    # 控制发送频率：存入redis,有效期设置为60秒
    caches["sms_code"].set(key, code_num, 60)
    # 验证码校验：存入redis,有效期设置为300秒
    key_verify = f"sms_{phone}_verify"
    caches["sms_code"].set(key_verify, code_num, 300)

    return JsonResponse({"code": 200, "data": "短信发送成功"})


class WeiBoCodeView(View):
    def get(self, request):
        """
        获取授权登录地址视图逻辑
        """
        oauth_url = f"https://api.weibo.com/oauth2/authorize?client_id={settings.CLIENT_ID}&redirect_uri={settings.REDIRECT_URI}&response_type=code"

        # 前端:window.location.href=response.oauth_url
        return JsonResponse({"code": 200, "oauth_url": oauth_url})


class WeiBoTokenView(View):
    def get(self, request):
        """
        获取访问令牌access_token视图逻辑
        依据微博接口文档
        """
        code = request.GET.get("code")
        url = "https://api.weibo.com/oauth2/access_token"
        data = {
            "client_id": settings.CLIENT_ID,
            "client_secret": settings.CLIENT_SECRET,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": settings.REDIRECT_URI,
        }

        html = requests.post(url=url, data=data).json()
        print("---------->", html)
        """
        {'access_token': '2.00UzNgEINgEQJEcd29cd3316a2zrCD', 
         'remind_in': '157679999', 
         'expires_in': 157679999, 
         'uid': '7398231560', 
         'isRealName': 'true'}
        """
        wuid = html.get("uid")
        access_token = html.get("access_token")
        """
        查询微博表中wuid这条数据是否存在(get(),注意加try语句)
        情况1:用户第一次扫码登录,返回201
        情况2:用户非第一次扫码登录(根据外键是否为空)
             2.1 已经做好绑定关系,返回200
             2.2 没有做好绑定关系,返回201
        """
        try:
            wuser = WeiBoProfile.objects.get(wuid=wuid)
        except Exception as e:
            WeiBoProfile.objects.create(wuid=wuid, access_token=access_token)
            return JsonResponse({"code": 201, "uid": wuid})

        # 非第一次扫码登录
        user = wuser.user_profile
        if user:
            # 做好绑定关系
            username = user.username
            token = make_token(username)
            return JsonResponse({"code": 200, "username": username, "token": token})

        return JsonResponse({"code": 201, "uid": wuid})

    def post(self, request):
        """
        绑定注册:没有达达账号,请注册视图逻辑
        1.获取请求体数据(username、password、email、phone、uid)
        2.数据合法性校验
        3.两个orm操作
          3.1 在用户表中存入数据
          3.2 更新微博表的外键
        4.返回响应 {"code":200,"username":xx,"token":xx}
        """
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        email = data.get("email")
        phone = data.get("phone")
        wuid = data.get("uid")

        # 数据合法性校验
        if len(username) < 6 or len(username) > 11:
            return JsonResponse({"code": 10118, "error": "用户名不合法"})

        if len(password) < 6 or len(password) > 12:
            return JsonResponse({"code": 10119, "error": "密码不合法"})

        if len(phone) != 11:
            return JsonResponse({"code": 10120, "error": "手机号不合法"})

        # 用户名是否被占用
        user_query = UserProfile.objects.filter(username=username)
        if user_query:
            return JsonResponse({"code": 10103, "error": "用户名被占用"})

        # 存入数据表、更新微博表外键
        with transaction.atomic():
            sid = transaction.savepoint()
            try:
                pwd_md5 = md5_func(password)
                user = UserProfile.objects.create(username=username, password=pwd_md5, email=email, phone=phone)
                # 绑定:更新微博表外键
                wuser = WeiBoProfile.objects.get(wuid=wuid)
                wuser.user_profile = user
                wuser.save()
            except Exception as e:
                # 回滚 + 返回
                transaction.savepoint_rollback(sid)
                return JsonResponse({"code": 10121, "error": "绑定失败,请重试"})
            # 提交事务
            transaction.savepoint_commit(sid)

        # 发送激活邮件
        verify_url = get_verify_url(username)
        send_active_email(email, username, verify_url)
        token = make_token(username)

        return JsonResponse({"code": 200, "username": username, "token": token})


class WeiBoBindView(View):
    def post(self, request):
        """
        已有用户请绑定视图逻辑
        1.请求体数据(username、password、uid)
        2.校验用户名和密码是否正确
          2.1 错误:{"code": 10115, "error":"用户名或密码错误"}
          2.2 正确,做绑定关系(更新微博表外键)
              {"code":200, "username":xx, "token":xx}
        """
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        wuid = data.get("uid")

        try:
            user = UserProfile.objects.get(username=username)
        except Exception as e:
            return JsonResponse({"code": 10116, "error": "用户名错误"})

        if user.password != md5_func(password):
            return JsonResponse({"code": 10117, "error": "用户名或密码错误"})

        # 绑定 - 更新微博表数据的外键(一查二改三保存)
        try:
            wuser = WeiBoProfile.objects.get(wuid=wuid)
        except Exception as e:
            return JsonResponse({"code": 10118, "error": "微博服务器繁忙,请再试一次~"})

        wuser.user_profile = user
        wuser.save()

        token = make_token(username)

        return JsonResponse({"code": 200, "username": username, "token": token})


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


def get_verify_url(username):
    """
    功能函数:获取邮件激活链接
    :return verify_url
    """
    code_num = random.randint(1000, 9999)
    code_str = f"{code_num}_{username}"
    code = base64.b64encode(code_str.encode()).decode()
    verify_url = f"http://127.0.0.1:7000/dadashop/templates/active.html?code={code}"

    # 存入redis: {"active_liying": 1016}
    key = f"active_{username}"
    caches["default"].set(key, code_num, 86400 * 3)

    return verify_url


