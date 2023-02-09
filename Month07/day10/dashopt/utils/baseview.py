import json

import jwt
from django.conf import settings
from django.http import JsonResponse
from django.views import View

from users.models import UserProfile


class BaseView(View):
    def dispatch(self, request, *args, **kwargs):
        # token校验逻辑
        token = request.META.get("HTTP_AUTHORIZATION")
        key = settings.JWT_TOKEN_KEY
        try:
            payload = jwt.decode(token, key, algorithms="HS256")
        except Exception as e:
            # token有问题!
            return JsonResponse({"code": 403})

        # 给所有套过此装饰器的request对象都额外增加了一个myuser属性
        username = payload.get("username")
        user = UserProfile.objects.get(username=username)
        request.myuser = user

        body_data = request.body
        if body_data:
            request.mydata = json.loads(body_data)

        return super().dispatch(request, *args, **kwargs)












