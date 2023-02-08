"""
    测试查询地址功能
"""
import requests

url = "http://127.0.0.1:8000/v1/users/zhaoliying/address"
headers = {"authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NzUzMjMyNzgsInVzZXJuYW1lIjoiemhhb2xpeWluZyJ9.fpyprPCzmIrrBII5_fxXVzS4As4ImDQwLN9bR_Cicvc"}
resp = requests.get(url=url, headers=headers).json()
print(resp)














