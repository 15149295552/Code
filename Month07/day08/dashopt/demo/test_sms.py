import requests

url = "http://127.0.0.1:8000/v1/users/sms/code"
data = {"phone": "13603263409"}
resp = requests.post(url=url, json=data).json()
print(resp)









