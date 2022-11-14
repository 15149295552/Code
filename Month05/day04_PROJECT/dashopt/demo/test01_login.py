"""
    测试达达商城 登录模块
"""
import requests


url = "http://127.0.0.1:8000/v1/users/login"
data = {
    "username": "zhaoliying",
    "password": "123456"
}
resp = requests.post(url=url, json=data)
print(resp.text)












