import hashlib


s = hashlib.sha256()
s.update(b"123456")
r = s.hexdigest()

# r: 字符串(md5 sha256 hmac-sha256)
print(r)













