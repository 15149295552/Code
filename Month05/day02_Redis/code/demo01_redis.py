import random
import redis
import time


# redis: redis-cli -h 127.0.0.1 -p 6379 -a
r = redis.Redis()
# r = redis.Redis(host="127.0.0.1", port=6379, db=0)
result = r.keys("*")
print([i.decode() for i in result])

r.set("index_cache", "<HttpResponse 200>", 300)
print(r.get("index_cache").decode())

# phone:13603263409   Send a random six code
# key: sms_13603263409
# value: 六位随机数
code = random.randint(100000, 999999)
r.set("sms_13603263409", code, 5)

# time.sleep(6)
redis_code = r.get("sms_13603263409")
if redis_code:
    print("验证码未过期")
else:
    print("验证码已过期,请重新获取")

# mset name ying age 35
r.mset({"name": "ying", "age": 35})
print(r.mget(["name", "age"]))

r.lpush("email_list", "1@qq.com", "2@qq.com")
print(r.lrange("email_list", 0, -1))










