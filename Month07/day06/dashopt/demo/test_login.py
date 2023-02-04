import requests

url = "http://127.0.0.1:8000/v1/users/login"
data = {
    "username": "zhaoliying",
    "password": "123456"
}
resp = requests.post(url=url, json=data).json()
print(resp)



















