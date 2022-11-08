import redis
import json


r = redis.Redis()

r.hset("carts_1", "pro_6", "[3, 1]")
r.hset("carts_1", mapping={"pro_5": "[2, 1]", "pro_8": "[2, 0]"})

dic = r.hgetall("carts_1")
# {b'pro_6': b'[3, 1]', b'pro_5': b'[2, 1]', b'pro_8': b'[2, 0]'}
print(dic)

# 字典推导式(可以查)
new_dic = {k.decode(): json.loads(v) for k, v in dic.items()}
# {'pro_6': [3, 1], 'pro_5': [2, 1], 'pro_8': [2, 0]}
print({k: v for k, v in new_dic.items() if v[1] == 1})

# 删除key: carts_1  Redis命令行: DEL key
r.delete("carts_1")





















