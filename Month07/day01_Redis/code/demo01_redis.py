import redis
import time

# 1.连接redis数据库: redis-cli -h 127.0.0.1 -p 6379
r = redis.Redis(host="127.0.0.1", port=6379, db=0)

# KEYS * [b'name', b'age', b'trill_stu', b'pwd']
result = r.keys("*")
print([i.decode() for i in result])

r.set("sms_13603263409", 871016, ex=5)
# time.sleep(6)
result = r.get("sms_13603263409")
if not result:
    print("验证码已过期,请重新获取!")
else:
    print(int(result.decode()))

r.mset({"index_cache": "index", "detail_cache": "detail"})
result = r.mget(["index_cache", "detail_cache"])
print([i.decode() for i in result])

# result: 0 | 1
result = r.delete("index_cache")
if result:
    print("缓存清除成功")
else:
    print("缓存清除失败")


r.lpush("spider", "task03", "task02", "task01")
result = r.lrange("spider", 0, -1)
print(result)

# result: (b'spider', b'task03')
result = r.brpop("spider", 3)
print(result)

length = r.llen("spider")
print(length)
















