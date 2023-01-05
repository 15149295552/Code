import hmac

r = hmac.new(key=b"123456", msg=b"liying", digestmod="SHA256").hexdigest()
print(r)















