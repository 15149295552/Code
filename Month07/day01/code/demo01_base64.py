import base64

# 1.编码
r = base64.b64encode(b"zhaoliying")
print(r.decode())

# 2.解码
r = base64.b64decode("eWluZ2h1b2Nob25n".encode())
print(r.decode())















