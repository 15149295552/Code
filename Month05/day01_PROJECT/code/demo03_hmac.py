import hmac

# key: 公司密钥
# msg: 欲加密的数据
# digestmod: 加密算法

r = hmac.new(key=b"!@#$%^&*()", msg=b"123456", digestmod="SHA256")
print(r.hexdigest())












