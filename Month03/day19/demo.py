import hashlib

pwd = input("密码：")

hash = hashlib.sha256() # 选择算法
hash.update(pwd.encode()) # 转换加密
print(hash.hexdigest()) # 获取结果