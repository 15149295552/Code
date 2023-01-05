"""
    生产者
"""
import redis

# 默认连接:本机6379端口db0库
r = redis.Redis()

r.lpush("tasks_list", "task01", "task02", "task03")








