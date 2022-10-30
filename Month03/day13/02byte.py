"""
关于字节串回顾
"""
# 定义字节串适用于英文
byte01 = b"Hello world"
print(type(byte01))

# 字符串转换为字节串
byte02 = "你好 中国".encode()
print(byte02)

# 字节串 -》 字符串
print(byte02.decode())
# print(b'\xe6\xb6\xa6\xe1\xa1\xb1 \xe4\xf8\xbb\xe5\x9b\xbd'.decode())