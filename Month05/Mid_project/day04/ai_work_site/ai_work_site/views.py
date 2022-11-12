import json
import time
import jwt
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.conf import settings



# 配置cors跨域后测试
def test_cors(request):
    return JsonResponse({'msg':'CORS is ok'})

#异常码 10200-10299
# Create your views here.
def tokens(request):

    if request.method != 'POST':
        result = {'code':10200, 'error':'Please use POST!'}
        return JsonResponse(result)
    json_str = request.body
    json_obj = json.loads(json_str)
    username = json_obj['username']
    password = json_obj['password']
    #校验用户名和密码
    if authenticate(username=username, password=password):
        # 记录会话状态
        token = make_token(username)
        result = {'code': 200, 'username': username, 'data': {'token': token}}
        return JsonResponse(result)
    else:
        result = {'code':10201, 'error':'The username or password is wrong'}
        return JsonResponse(result)



def make_token(username, expire=3600*24):

    key = settings.JWT_TOKEN_KEY
    now_t = time.time()
    payload_data = {'username':username, 'exp':now_t+expire}
    return jwt.encode(payload_data, key, algorithm='HS256')

