import redis

r = redis.Redis(host="127.0.0.1", port=6379, db=0)

r.sadd("武将", "张飞", "许褚", "赵云", "马超", "周瑜")
r.sadd("文臣", "诸葛亮", "周瑜", "司马懿")

# 1.差集 sdiff
data1 = r.sdiff("武将", "文臣")
print({s.decode() for s in data1})

# 2.交集 sinter
data2 = r.sinter("武将", "文臣")
print({s.decode() for s in data2})

# 3.并集 sunion
data3 = r.sunion("武将", "文臣")
print({s.decode() for s in data3})















