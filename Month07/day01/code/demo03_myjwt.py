import base64
import hmac
import time
import json

# 1.生成token
header = {"alg": "HS256", "typ": "JWT"}
header_str = json.dumps(header)
header_bs = base64.b64encode(header_str.encode())

payload = {
    "exp": int(time.time()) + 5,
    "username": "zhaoliying"
}
payload_str = json.dumps(payload)
payload_bs = base64.b64encode(payload_str.encode())

key = b"123456"
msg = header_bs + b"." + payload_bs
sign_str = hmac.new(key=key, msg=msg, digestmod="SHA256").hexdigest()
sign_bs = base64.b64encode(sign_str.encode())

token = msg + b"." + sign_bs
print(token)

# 2.校验token
#   2.1 合法性
#   token: b"xxx.yyy.zzz"
time.sleep(6)
x, y, z = token.split(b".")
sign_user = hmac.new(key=key, msg=x + b"." + y, digestmod="SHA256").hexdigest()
sign_user = base64.b64encode(sign_user.encode())
if sign_user != z:
    print("token不合法")

#   2.2 有效期
#   payload: '{"exp": xxx, "username": xxx}'
payload = base64.b64decode(y).decode()
#   payload: {"exp": xxx, "username": xxx}
payload = json.loads(payload)
exp = payload.get("exp")
now = time.time()

# exp: 6666
# now: 6668
if now > exp:
    print("已过期,请重新登录")

username = payload.get("username")
# 执行具体的业务逻辑,比如查询订单、查询购物车... ...












