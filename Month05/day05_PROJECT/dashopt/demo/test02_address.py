"""
    测试查询地址功能
"""
import requests

url = "http://127.0.0.1:8000/v1/users/zhaoliying/address"
headers = {"authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Njg0ODQ0MDksInVzZXJuYW1lIjoiemhhb2xpeWluZyJ9.yLWrB6lameET43ypJPSFbcW8WuKe8cczc3kSJ562dDI"}

resp = requests.get(url=url, headers=headers)
print(type(resp.text), resp.text)
print(type(resp.json()), resp.json())











