"""
    python操作有序集合
"""
import redis

r = redis.Redis()

# ZADD key score member score member ...
r.zadd("play:number", {"小燕子": 100, "小白兔": 200, "春天在哪里": 300})

# ZRANGE key start stop withscores
# print(r.zrange("play:number", 0, -1, withscores=True))

r.zadd("play:number2", {"小燕子": 500, "活着": 2000, "海阔天空": 30000})


# 并集:不带权重
r.zunionstore("union_play", ["play:number", "play:number2"], aggregate="SUM")
data = r.zrange("union_play", 0, -1, withscores=True)

for t in data:
    print(t[0].decode(), int(t[1]))

# 并集:带权重

r.zunionstore("union_play2", {"play:number": 0.5, "play:number2": 0.5}, aggregate="SUM")
data = r.zrange("union_play2", 0, -1, withscores=True)

for t in data:
    print(t[0].decode(), int(t[1]))









