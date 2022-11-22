import base64

username = "zhaoliying"

# 1.编码
result = base64.b64encode(username.encode())
print(result.decode())

# 2.解码
r = base64.b64decode(result)
print(r.decode())
