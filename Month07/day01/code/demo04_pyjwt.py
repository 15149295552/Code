import jwt
import time

# 1.生成token
payload = {
    "exp": int(time.time()) + 5,
    "username": "zhaoliying"
}
key = "123456"
token = jwt.encode(payload=payload, key=key, algorithm="HS256")
print(token)

# 2.校验token
# time.sleep(6)
try:
    payload = jwt.decode(token, key, algorithms="HS256")
    print(payload)
except:
    print("重新登录")








