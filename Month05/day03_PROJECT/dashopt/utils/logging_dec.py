"""
    装饰器:用户登录状态的校验
"""
import jwt
from django.conf import settings
from django.http import JsonResponse

from users.models import UserProfile


def logging_check(func):
    def wrapper(self, request, *args, **kwargs):
        """
        1.获取token
        2.校验token
          校验失败:直接返回{"code":403}
          校验成功:执行视图函数func
        """
        token = request.META.get("HTTP_AUTHORIZATION")
        key = settings.JWT_TOKEN_KEY
        try:
            payload = jwt.decode(token, key, algorithms="HS256")
        except Exception as e:
            return JsonResponse({"code": 403})

        username = payload.get("username")
        user = UserProfile.objects.get(username=username)
        request.myuser = user

        return func(self, request, *args, **kwargs)
    return wrapper

















