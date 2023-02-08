"""
测试达达商城注册功能(依据API文档)
"""
import requests

url = "http://127.0.0.1:8000/v1/users/register"
data = {
    'uname': 'dilireba',
    'password': '123456',
    'phone': '13603263333',
    'email': '309435365@qq.com',
    'verify': '123456',
}

resp = requests.post(url=url, json=data).json()
print(resp)






