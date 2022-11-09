import time
import jwt

payload = {
    "exp": int(time.time()) + 5,
    "username": "ying"
}
key = "1234567890"

# 1.生成token
token = jwt.encode(payload=payload, key=key, algorithm="HS256")
print(token)

# 2.校验token
# time.sleep(6)
payload = jwt.decode(token, key, algorithms="HS256")
print(payload)











