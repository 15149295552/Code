import jwt
from django.conf import settings
from django.http import JsonResponse


def logging_check(func):
    def wrapper(self, request, *args, **kwargs):
        """
        1.获取token
        2.校验token
          2.1 校验失败: return {"code": 403}
          2.2 校验成功: 走对应视图逻辑 func(self, ....)
        """
        # DJANGO会把所有请求头都大写,并加上HTTP_前缀
        token = request.META.get("HTTP_AUTHORIZATION")
        key = settings.JWT_TOKEN_KEY
        try:
            payload = jwt.decode(token, key, algorithms="HS256")
        except Exception as e:
            # token有问题!
            return JsonResponse({"code": 403})

        return func(self, request, *args, **kwargs)
    return wrapper











