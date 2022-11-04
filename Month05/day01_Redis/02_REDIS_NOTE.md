[toc]

# 1. Redis基础

## 1）Redis介绍

- **特点及优点**

```python
1、开源的，使用C编写，基于内存且支持持久化
2、高性能的Key-Value的NoSQL数据库
3、支持数据类型丰富，字符串strings，散列hashes，列表lists，集合sets，有序集合sorted sets 等等
4、支持多种编程语言（C C++ Python Java PHP ... ）
5、单进程单线程
```

- **与其他数据库对比**

```python
1、MySQL : 关系型数据库，表格，基于磁盘，慢
2、MongoDB：键值对文档型数据库，值为类似JSON文档，数据结构相对单一
3、Redis的诞生是为了解决什么问题？？
   # 解决硬盘IO带来的性能瓶颈
```

- **应用场景**

```python
1，缓存
2，并发计数
3，排行榜
4，生产者消费者模型
...
```

- **redis版本**

```python
1、最新版本：6.0
2、常用版本：2.4、2.6、2.8、3.0(里程碑)、3.2、3.4、4.0、5.0、6.0(教学环境版本)
```

- **Redis附加功能**

```python
1、持久化
  将内存中数据保存到磁盘中，保证数据安全，方便进行数据备份和恢复
2、过期键功能
   为键设置一个过期时间，让它在指定时间内自动删除
   <节省内存空间>
   # 音乐播放器，日播放排名，过期自动删除
3、事务功能
   原子的执行多个操作
4、主从复制
5、Sentinel哨兵
```

## 2）安装

- Ubuntu

```python
# 安装
sudo apt-get install redis-server
# 服务端启动
sudo /etc/init.d/redis-server status | start | stop | restart
# 测试性能
redis-benchmark -q -n 10000
# 客户端连接
redis-cli -h IP地址 -p 6379 -a 密码
```

## 3）配置文件详解

- **配置文件所在路径**

```python
/etc/redis/redis.conf
mysql的配置文件在哪里？ : /etc/mysql/mysql.conf.d/mysqld.cnf
```

- **设置连接密码**

```python
1、requirepass 密码   #790行
2、重启服务
   sudo /etc/init.d/redis-server restart
3、客户端连接
   redis-cli -h 127.0.0.1 -p 6379 -a 123456
   127.0.0.1:6379>ping
```

- **允许远程连接**

```python
1、注释掉本地IP地址绑定
  68行: # bind 127.0.0.1 ::1
2、关闭保护模式(把yes改为no)
  87行: protected-mode no
3、重启服务
  sudo /etc/init.d/redis-server restart
```

- **通用命令 ==适用于所有数据类型==**

```python
# 切换库(number的值在0-15之间,db0 ~ db15)
select number
# 查看键
keys 表达式  # keys *
# 数据类型
type key
# 键是否存在
exists key
# 删除键
del key
# 键重命名
rename key newkey
# 清除当前库中所有数据（慎用）
flushdb
# 清除所有库中所有数据（慎用）
flushall
```



## 4）数据类型

### 4.1 字符串类型(string)

- **特点**

```python
1、字符串、数字，都会转为字符串来存储
2、以二进制的方式存储在内存中
```

- **字符串常用命令-==必须掌握==**

```python
# 1. 设置一个key-value
set key value
# 2. 获取key的值
get key
# 3. key不存在时再进行设置(nx)
set key value nx  # not exists
# 4. 设置过期时间(ex)
set key value ex seconds

# 5. 同时设置多个key-value
mset key1 value1 key2 value2 key3 value3
# 6. 同时获取多个key-value
mget key1 key2 key3 
```

- **数值操作-==字符串类型数字(必须掌握)==**

```python
# 整数操作
incrby key 步长
decrby key 步长
incr key : +1操作
decr key : -1操作
# 应用场景: 抖音上有人关注你了，是不是可以用INCR呢，如果取消关注了是不是可以用DECR
# 浮点数操作: 自动先转为数字类型，然后再进行相加减，不能使用append
incrbyfloat key step
```

- **设置过期时间**
```python
# 设置过期时间的两种方式
# 方式一
1、set key value ex 3
# 方式二
1、set key value
2、expire key 5 # 秒
3、pexpire key 5 # 毫秒
# 查看存活时间
ttl key
# 删除过期
persist key
```

- **string数据类型注意**

```python
# key命名规范
可采用 - wang:email
# key命名原则
1、key值不宜过长，消耗内存，且在数据中查找这类键值的计算成本高
2、不宜过短，可读性较差
# 值
1、一个字符串类型的值最多能存储512M内容
```

- 业务场景
  - 缓存
    - 将mysql中的数据存储到redis字符串类型中
  - 并发计数 - 点赞/秒杀
    - 说明：通过redis单进程单线程的特点，由redis负责计数，并发问题转为串行问题
  - 带有效期的验证码  - 短信验证码
    - 借助过期时间，存放验证码；到期后，自动消亡

**练习**

```python
1、查看 db0 库中所有的键
  # SELECT 0
  # KEYS *
2、设置键 trill:username 对应的值为 user001，并查看
  # SET trill:username user001
3、获取 trill:username 值的长度 
  # STRLEN trill:username
4、一次性设置 trill:password 、trill:gender、trill:fansnumber 并查看（值自定义）     
  # MSET trill:password 123456 trill:gender M trill:fansnumber 100
5、查看键 trill:score 是否存在 
  # EXISTS trill:score
6、增加10个粉丝
  # INCRBY trill:fansnumber 10
7、增加2个粉丝（一个一个加）
  # INCR trill:fansnumber
  # INCR trill:fansnumber
8、有3个粉丝取消关注你了
  # DECRBY trill:fansnumber 3
9、又有1个粉丝取消关注你了
  # DECR trill:fansnumber 
10、思考、思考、思考...,清除当前库
  # FLUSHDB
11、一万个思考之后，清除所有库
  # FLUSHALL
```

### 4.2 列表数据类型（List）

- **特点**

```python
1、元素是字符串类型
2、列表头尾增删快，中间增删慢，增删元素是常态
3、元素可重复
4、最多可包含2^32 -1个元素
5、索引同python列表
```

- **列表常用命令**

```python
# 增
1、从列表头部压入元素
	LPUSH key value1 value2 
    返回：list长度
2、从列表尾部压入元素
	RPUSH key value1 value2
    返回：list长度
3、从列表src尾部弹出1个元素,压入到列表dst的头部
	RPOPLPUSH src dst
    返回：被弹出的元素
4、在列表指定元素后/前插入元素
	LINSERT key after|before value newvalue
    返回：
		1，如果命令执行成功，返回列表的长度
		2，如果没有找到 pivot ，返回 -1
		3，如果 key 不存在或为空列表，返回 0 

# 查
5、查看列表中元素
	LRANGE key start stop
  # 查看列表中所有元素: LRANGE key 0 -1
6、获取列表长度
	LLEN key

# 删
7、从列表头部弹出1个元素
	LPOP key
8、从列表尾部弹出1个元素
	RPOP key
9、列表头部,阻塞弹出,列表为空时阻塞
	BLPOP key timeout
10、列表尾部,阻塞弹出,列表为空时阻塞
	BRPOP key timeout
  # 关于BLPOP 和 BRPOP
  	1、如果弹出的列表不存在或者为空，就会阻塞
	2、超时时间设置为0，就是永久阻塞，直到有数据可以弹出
	3、如果多个客户端阻塞再同一个列表上，使用First In First Service原则，先到先服务
11、删除指定元素
	LREM key count value
    count>0：表示从头部开始向表尾搜索，移除与value相等的元素，数量为count
	count<0：表示从尾部开始向表头搜索，移除与value相等的元素，数量为count
	count=0：移除表中所有与value相等的值
    返回：被移除元素的数量
    
12、保留指定范围内的元素
	LTRIM key start stop
    返回：ok
    样例：
  		LTRIM mylist1 0 2 # 只保留前3条
  		# 应用场景: 保存微博评论最后500条
  		LTRIM weibo:comments 0 499
	# 改
13、将列表 key 下标为 index 的元素的值设置为 value
	LSET key index newvalue
```

**练习**

```python
1、查看所有的键
  # KEYS *
2、向列表 spider:urls 中以RPUSH放入如下几个元素：01_baidu.com、02_taobao.com、03_sina.com、04_jd.com、05_xxx.com
  # RPUSH spider:urls 01_baidu.com 02_taobao.com 03_sina.com 04_jd.com 05_xxx.com
3、查看列表中所有元素
  # LRANGE spider:urls 0 -1
4、查看列表长度
  # LLEN spider:urls
5、将列表中01_baidu.com 改为 01_tmall.com
  # LSET spider:urls 0 01_tmall.com
6、在列表中04_jd.com之后再加1个元素 02_taobao.com
  # LINSERT spider:urls after 04_jd.com 02_taobao.com
7、弹出列表中的最后一个元素
  # RPOP spider:urls 
8、删除列表中所有的 02_taobao.com
  # LREM spider:urls 0 02_taobao.com
9、剔除列表中的其他元素，只剩前3条
  # LTRIM spider:urls 0 2
```



## 5）python交互redis

- **模块(redis)**

Ubuntu

```python
sudo pip3 install redis
```

- **使用流程**

```python
import redis
# 创建数据库连接对象
r = redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')
```

- **代码示例**

```python
import redis

# 1 创建redis数据库连接对象
r = redis.Redis()
# 2 使用,很多命令的返回值是字节串,需要用字符串
#  表示时,调用decode方法.
# 3.1 通用命令...
print(r.keys('*'))
print(r.exists('name'))
# 3.2 字符串类型的操作
r.set('uname', 'aid2102', 60)
print(r.get('uname').decode())
r.mset({'a': 100, 'b': 200, 'c': 300})
print(r.mget(['a', 'b', 'c']))
# 3.3 列表类型的操作
r.lpush('pylk1',100,200,300)
print(r.lrange('pylk1',0,-1))
```
## 6）Hash散列数据类型

- **定义**

```python
1、由field和关联的value组成的键值对
2、field和value是字符串类型
3、一个hash中最多包含2^32-1个键值对
```

- **优点**

```python
1、节约内存空间 - 特定条件下 【1，字段小于512个，2：value不能超过64字节】
2、可按需获取字段的值
```

- **缺点（不适合hash情况）**

```python
1，使用过期键功能：键过期功能只能对键进行过期操作，而不能对散列的字段进行过期操作
2，存储消耗大于字符串结构
```

- **基本命令操作**

```python
# 1、设置单个字段
HSET key field value
HSETNX key field value
# 2、设置多个字段
HMSET key field value field value
# 3、返回字段个数
HLEN key
# 4、判断字段是否存在（不存在返回0）
HEXISTS key field
# 5、返回字段值
HGET key field
# 6、返回多个字段值
HMGET key field filed
# 7、返回所有的键值对
HGETALL key
# 8、返回所有字段名
HKEYS key
# 9、返回所有值
HVALS key
# 10、删除指定字段
HDEL key field 
# 11、在字段对应值上进行整数增量运算
HINCRBY key field increment
# 12、在字段对应值上进行浮点数增量运算
HINCRBYFLOAT key field increment
```

**python操作hash**

```python
# 1、更新一条数据的属性，没有则新建
hset(name, key, value) 
# 2、读取这条数据的指定属性， 返回字符串类型
hget(name, key)
# 3、批量更新数据（没有则新建）属性,参数为字典
hmset(name, mapping)
# 4、批量读取数据（没有则新建）属性
hmget(name, keys)
# 5、获取这条数据的所有属性和对应的值，返回字典类型
hgetall(name)
# 6、获取这条数据的所有属性名，返回列表类型
hkeys(name)
# 7、删除这条数据的指定属性
hdel(name, *keys)
```

**应用场景：用户维度数据统计**

```python
用户维度统计
   统计数包括：关注数、粉丝数、喜欢商品数、发帖数
   用户为key，不同维度为field，value为统计数
   比如关注了5人
	 HSET user:10000 fans 5
	 HINCRBY user:10000 fans 1
```

**python操作hash**

```python
import redis

# 创建redis数据库的连接对象
r = redis.Redis()

# 操作hash
r.hset('pyhk1', 'username', 'aid2212')
r.hmset('pyhk1', {'age': 18, 'major': 'python'})
print(r.hget('pyhk1', 'username').decode())
print(r.hmget('pyhk1', ['username', 'age']))
print(r.hgetall('pyhk1'))
# 字典推导式
data = {k.decode(): v.decode() for k, v in r.hgetall('pyhk1').items()}
print(data)
r.hdel('pyhk1','age')
print(r.hgetall('pyhk1'))
# 删除键
r.delete('pyhk1')
```

## 7）集合数据类型（set）

- **特点**

```python
1、无序、去重
2、元素是字符串类型
3、最多包含2^32-1个元素
```

- **基本命令**

```python
# 1、增加一个或者多个元素,自动去重；返回值为成功插入到集合的元素个数
SADD key member1 member2
# 2、查看集合中所有元素
SMEMBERS key
# 3、删除一个或者多个元素，元素不存在自动忽略
SREM key member1 member2
# 4、元素是否存在
SISMEMBER key member
# 5、随机返回集合中指定个数的元素，默认为1个
SRANDMEMBER key [count]
# 6、弹出成员
SPOP key [count]
# 7、返回集合中元素的个数，不会遍历整个集合，只是存储在键当中了
SCARD key
# 8、把元素从源集合移动到目标集合
SMOVE source destination member

# 9、差集(number1 1 2 3 number2 1 2 4 结果为3)
SDIFF key1 key2 
# 10、差集保存到另一个集合中
SDIFFSTORE destination key1 key2

# 11、交集
SINTER key1 key2
SINTERSTORE destination key1 key2

# 11、并集
SUNION key1 key2
SUNIONSTORE destination key1 key2
```

**案例: 新浪微博的共同关注**

```python
# 需求: 当用户访问另一个用户的时候，会显示出两个用户共同关注过哪些相同的用户
# 设计: 将每个用户关注的用户放在集合中，求交集即可
# 实现:
	user001 = {'peiqi','qiaozhi','danni'}
	user002 = {'peiqi','qiaozhi','lingyang'}
  
user001和user002的共同关注为:
	SINTER user001 user002
	结果为: {'peiqi','qiaozhi'}
```

**python操作set**

```python
import redis

r = redis.Redis()
'''
   武将: 张飞 许褚 赵云 马超 周瑜
   文臣: 诸葛亮 周瑜 司马懿
   结果: 1.纯武将 2.纯文臣  3.文武双全  4.文臣武将
'''
# set集合类型的操作
r.sadd('武将', '张飞', '许褚', '赵云', '马超', '周瑜')
r.sadd('文臣', '诸葛亮', '周瑜', '司马懿')
data1 = r.sdiff('武将', '文臣')
result = []
for item in data1:
    result.append(item.decode())
print('纯武将:', result)

data2 = r.sdiff('文臣', '武将')
result = []
for item in data2:
    result.append(item.decode())
print('纯文臣:', result)

data3 = r.sinter('文臣', '武将')
result = []
for item in data3:
    result.append(item.decode())
print('文武双全:', result)

data4 = r.sunion('文臣', '武将')
result = []
for item in data4:
    result.append(item.decode())
print('文臣武将:', result)
```



## 8）有序集合sortedset

- **特点**

```
1、有序、去重
2、元素是字符串类型
3、每个元素都关联着一个浮点数分值(score)，并按照分值从小到大的顺序排列集合中的元素（分值可以相同）
4、最多包含2^32-1元素
```

- 示例

  **一个保存了水果价格的有序集合**

| 分值 | 2.0  | 4.0  | 6.0  | 8.0  | 10.0 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 元素 | 西瓜 | 葡萄 | 芒果 | 香蕉 | 苹果 |

​	**一个保存了员工薪水的有序集合**

| 分值 | 6000 | 8000 | 10000 | 12000 |
| ---- | ---- | ---- | ----- | ----- | 
| 元素 | lucy | tom  | jim   | jack  |

- **有序集合常用命令**

```python
# 在有序集合中添加一个成员 返回值为 成功插入到集合中的元素个数
zadd key score member
# 查看指定区间元素（升序)
zrange key start stop [withscores]
# 查看指定区间元素（降序）
zrevrange key start stop [withscores]
# 查看指定元素的分值
zscore key member

# 返回指定区间元素
# offset : 跳过多少个元素
# count : 返回几个
# 小括号 : 开区间  zrangebyscore fruits (2.0 8.0
zrangebyscore key min max [withscores] [limit offset count]
# 每页显示10个成员,显示第5页的成员信息: 
# limit 40 10
# MySQL: 每页显示10条记录,显示第5页的记录
# limit 40,10
# limit 2,3   显示: 第3 4 5条记录

# 删除成员
zrem key member
# 增加或者减少分值
zincrby key increment member
# 返回元素排名
zrank key member
# 返回元素逆序排名
zrevrank key member
# 删除指定区间内的元素
zremrangebyscore key min max
# 返回集合中元素个数
zcard key
# 返回指定范围中元素的个数
zcount key min max
zcount salary 6000 8000 
zcount salary (6000 8000# 6000<salary<=8000
zcount salary (6000 (8000#6000<salary<8000               
# 并集
zunionstore destination numkeys key [weights 权重值] [AGGREGATE SUM|MIN|MAX]
# zunionstore salary3 2 salary salary2 weights 1 0.5 AGGREGATE MAX
# 2代表集合数量,weights之后 权重1给salary,权重0.5给salary2集合,算完权重之后执行聚合AGGREGATE
                     
# 交集：和并集类似，只取相同的元素
zinterstore destination numkeys key1 key2 weights weight AGGREGATE SUM(默认)|MIN|MAX
```

**python操作sorted set**

```python
import redis

r = redis.Redis()

# 有序集合类型的操作
r.zadd('pyzk1', {'tedu': 100, 'tedu2': 200})
print(r.zrange('pyzk1', 0, -1, withscores=True))
r.zadd('pyzk2', {'tedu2': 200, 'tedu3': 200})
# 并集运算
r.zunionstore('pyzk3',['pyzk1','pyzk2'], aggregate='sum')
print(r.zrange('pyzk3', 0, -1, withscores=True))
# 并集运算(带权重)
r.zunionstore('pyzk4',{'pyzk1':0.8,'pyzk2':0.2},
              aggregate='sum')
print(r.zrange('pyzk4', 0, -1, withscores=True))

```



## 9）数据类型总结

<font color=red>**五大数据类型及应用场景**</font>

| 类型       | 特点                                                         | 使用场景                                                     |
| :--------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| string     | 简单key-value类型，value可为字符串和数字                     | 常规计数（微博数, 粉丝数等功能）                             |
| hash       | 是一个string类型的field和value的映射表，hash特别适合用于存储对象 | 存储部分可能需要变更的数据（比如用户信息）                   |
| list       | 有序可重复列表                                               | 消息队列等                                                   |
| set        | 无序不可重复列表                                             | 存储并计算关系（如微博，关注人或粉丝存放在集合，可通过交集、并集、差集等操作实现如共同关注、共同喜好等功能） |
| sorted set | 每个元素带有分值的集合                                       | 各种排行榜                                                   |

# 2. Redis高级
## 1）数据持久化

**持久化定义**

```python
将数据从掉电易失的内存放到永久存储的设备上
```

**为什么需要持久化**

```python
因为所有的数据都在内存上，所以必须得持久化
```

### 1.1 RDB模式（默认开启）

```python
1、保存真实的数据
2、将服务器包含的所有数据库数据以二进制文件的形式保存到硬盘里面
3、默认文件名 ：/var/lib/redis/dump.rdb
```

**创建rdb文件的两种方式**

**方式一：**redis终端中使用SAVE或者BGSAVE命令

```python
127.0.0.1:6379> SAVE
OK
# 特点
1、执行SAVE命令过程中，redis服务器将被阻塞，无法处理客户端发送的命令请求，在SAVE命令执行完毕后，服务器才会重新开始处理客户端发送的命令请求
2、如果RDB文件已经存在，那么服务器将自动使用新的RDB文件代替旧的RDB文件
# 工作中定时持久化保存一个文件

127.0.0.1:6379> BGSAVE
Background saving started
# 执行过程如下
1、客户端 发送 BGSAVE 给服务器
2、服务器马上返回 Background saving started 给客户端
3、服务器 fork() 子进程做这件事情
4、服务器继续提供服务
5、子进程创建完RDB文件后再告知Redis服务器

# 配置文件相关
/etc/redis/redis.conf
365行: dir /var/lib/redis # 表示rdb文件存放路径
342行: dbfilename dump.rdb  # 文件名

# 两个命令比较
SAVE比BGSAVE快，因为需要创建子进程，消耗额外的内存

# 补充：可以通过查看日志文件来查看redis都做了哪些操作
# 日志文件：配置文件中搜索 logfile
logfile /var/log/redis/redis-server.log
```

**方式二：**设置配置文件条件满足时自动保存**（使用最多）**

```python
# redis配置文件默认
307行: save 900 1
308行: save 300 10
    表示如果距离上一次创建RDB文件已经过去了300秒，并且服务器的所有数据库总共已经发生了不少于10次修改，那么自动执行BGSAVE命令
309行: save 60 10000
  1、只要三个条件中的任意一个被满足时，服务器就会自动执行BGSAVE
  2、每次创建RDB文件之后，服务器为实现自动持久化而设置的时间计数器和次数计数器就会被清零，并重新开始计数，所以多个保存条件的效果不会叠加
    
# 该配置项也可以在命令行执行 [不推荐] 
redis>save 60 10000
```

**RDB缺点**

```shell
1、创建RDB文件需要将服务器所有的数据库的数据都保存起来，这是一个非常消耗资源和时间的操作，所以服务器需要隔一段时间才创建一个新的RDB文件，也就是说，创建RDB文件不能执行的过于频繁，否则会严重影响服务器的性能
2、可能丢失数据
```



### 1.2 AOF（AppendOnlyFile）

```python
1、存储的是命令，而不是真实数据
2、默认不开启
# 开启方式（修改配置文件）
1、/etc/redis/redis.conf
  1094行: appendonly yes # 把 no 改为 yes
  1098行: appendfilename "appendonly.aof"
2、重启服务
  sudo /etc/init.d/redis-server restart
```

**AOF持久化原理及优点**

```python
# 原理
   1、每当有修改数据库的命令被执行时， 
   2、因为AOF文件里面存储了服务器执行过的所有数据库修改的命令，所以给定一个AOF文件，服务器只要重新执行一遍AOF文件里面包含的所有命令，就可以达到还原数据库的目的

# 优点
  用户可以根据自己的需要对AOF持久化进行调整，让Redis在遭遇意外停机时不丢失任何数据，或者只丢失一秒钟的数据，这比RDB持久化丢失的数据要少的多
```

**特殊说明**

```python
# 因为
  虽然服务器执行一个修改数据库的命令，就会把执行的命令写入到AOF文件，但这并不意味着AOF文件持久化不会丢失任何数据，在目前常见的操作系统中，执行系统调用write函数，将一些内容写入到某个文件里面时，为了提高效率，系统通常不会直接将内容写入硬盘里面，而是将内容放入一个内存缓存区（buffer）里面，等到缓冲区被填满时才将存储在缓冲区里面的内容真正写入到硬盘里

# 所以
  1、AOF持久化：当一条命令真正的被写入到硬盘里面时，这条命令才不会因为停机而意外丢失
  2、AOF持久化在遭遇停机时丢失命令的数量，取决于命令被写入到硬盘的时间
  3、越早将命令写入到硬盘，发生意外停机时丢失的数据就越少，反之亦然
```

**策略 - 配置文件**

```python
# 打开配置文件:/etc/redis/redis.conf，找到相关策略如下
1、1123行: alwarys
   服务器每写入一条命令，就将缓冲区里面的命令写入到硬盘里面，服务器就算意外停机，也不会丢失任何已经成功执行的命令数据
2、1124行: everysec（# 默认）
   服务器每一秒将缓冲区里面的命令写入到硬盘里面，这种模式下，服务器即使遭遇意外停机，最多只丢失1秒的数据
3、1125行: no
   服务器不主动将命令写入硬盘,由操作系统决定何时将缓冲区里面的命令写入到硬盘里面，丢失命令数量不确定

# 运行速度比较
always：速度慢
everysec和no都很快，默认值为everysec
```

**AOF重写**

**思考：AOF文件中是否会产生很多的冗余命令？**

```python
为了让AOF文件的大小控制在合理范围，避免胡乱增长，redis提供了AOF重写功能，通过这个功能，服务器可以产生一个新的AOF文件
  -- 新的AOF文件记录的数据库数据和原由的AOF文件记录的数据库数据完全一样
  -- 新的AOF文件会使用尽可能少的命令来记录数据库数据，因此新的AOF文件的提及通常会小很多
  -- AOF重写期间，服务器不会被阻塞，可以正常处理客户端发送的命令请求
```

**示例**

| 原有AOF文件                | 重写后的AOF文件                         |
| -------------------------- | --------------------------------------- |
| select 0                   | SELECT 0                                |
| sadd myset peiqi           | SADD myset peiqi qiaozhi danni lingyang |
| sadd myset qiaozhi         | SET msg 'hello tarena'                  |
| sadd myset danni           | RPUSH mylist 2 3 5                      |
| sadd myset lingyang        |                                         |
| INCR number                |                                         |
| INCR number                |                                         |
| DEL number                 |                                         |
| SET message 'hello world'  |                                         |
| SET message 'hello tarena' |                                         |
| RPUSH mylist 1 2 3         |                                         |
| RPUSH mylist 5             |                                         |
| LPOP mylist                |                                         |

**AOF重写-触发**

```python
1、客户端向服务器发送BGREWRITEAOF命令
   127.0.0.1:6379> BGREWRITEAOF
   Background append only file rewriting started

2、修改配置文件让服务器自动执行BGREWRITEAOF命令
  1165行：auto-aof-rewrite-percentage 100 
  1166行：auto-aof-rewrite-min-size 64mb 
  # 解释
    1、只有当AOF文件的增量大于100%时才进行重写，也就是大一倍的时候才触发
        # 第一次重写新增：64M
        # 第二次重写新增：128M
        # 第三次重写新增：256M（新增128M）
```



**RDB和AOF持久化对比**

| RDB持久化                                                    | AOF持久化                                     |
| ------------------------------------------------------------ | --------------------------------------------- |
| 全量备份，一次保存整个数据库                                 | 增量备份，一次保存一个修改数据库的命令        |
| 保存的间隔较长                                               | 保存的间隔默认为一秒钟                        |
| 数据还原速度快                                               | 数据还原速度一般，冗余命令多，还原速度慢      |
| 执行SAVE命令时会阻塞服务器，但手动或者自动触发的BGSAVE不会阻塞服务器 | 无论是平时还是进行AOF重写时，都不会阻塞服务器 |
|                                                              |                                               |

```python
# 用redis用来存储真正数据，每一条都不能丢失，都要用always，有的做缓存，有的保存真数据，我可以开多个redis服务，不同业务使用不同的持久化，新浪每个服务器上有4个redis服务，整个业务中有上千个redis服务，分不同的业务，每个持久化的级别都是不一样的。
```

**数据恢复（无需手动操作）**

```python
既有dump.rdb，又有appendonly.aof，恢复时找谁？
先找appendonly.aof
```

**配置文件常用配置总结**

```python
# 设置密码
1、requirepass password
# 开启远程连接
2、bind 127.0.0.1 ::1 注释掉
3、protected-mode no  把默认的 yes 改为 no
# rdb持久化-默认配置
4、dbfilename 'dump.rdb'
5、dir /var/lib/redis
# rdb持久化-自动触发(条件)
6、save 900 1
7、save 300 10 
8、save 60  10000
# aof持久化开启
9、appendonly yes
10、appendfilename 'appendonly.aof'
# aof持久化策略
11、appendfsync always
12、appendfsync everysec # 默认
13、appendfsync no
# aof重写触发
14、auto-aof-rewrite-percentage 100
15、auto-aof-rewrite-min-size 64mb
# 设置为从服务器
16、salveof <master-ip> <master-port>
```

**Redis相关文件存放路径**

```python
1、配置文件: /etc/redis/redis.conf
2、备份文件: /var/lib/redis/*.rdb|*.aof
3、日志文件: /var/log/redis/redis-server.log
4、启动文件: /etc/init.d/redis-server
# /etc/下存放配置文件
# /etc/init.d/下存放服务启动文件
```



## 2）Redis主从复制

- **定义**

```python
1、一个Redis服务可以有多个该服务的复制品，这个Redis服务成为master，其他复制品成为slaves
2、master会一直将自己的数据更新同步给slaves，保持主从同步
3、只有master可以执行写命令，slave只能执行读命令
```

- **作用**

```python
分担了读的压力（高并发）
```

- **原理**

```python
从服务器执行客户端发送的读命令，比如GET、LRANGE、SMEMMBERS、HGET、ZRANGE等等，客户端可以连接slaves执行读请求，来降低master的读压力
```

- **实现方式**

  ```shell
  # 两条命令
  1、>slaveof IP PORT
  2、>slaveof no one
  
  # 服务端启动
  redis-server --port 6301
  # 客户端连接
  tarena@tedu:~$ redis-cli -p 6301
  127.0.0.1:6301> keys *
  1) "myset"
  2) "mylist"
  127.0.0.1:6301> set mykey 123
  OK
  # 切换为从
  127.0.0.1:6301> slaveof 127.0.0.1 6379
  OK
  127.0.0.1:6301> set newkey 456
  (error) READONLY You can't write against a read only slave.
  127.0.0.1:6301> keys *
  1) "myset"
  2) "mylist" 
  # 再切换为主
  127.0.0.1:6301> slaveof no one
  OK
  127.0.0.1:6301> set name hello
  OK
  
  ```

**问题：master挂了怎么办？**

```python
1、一个Master可以有多个Slaves
2、Slave下线，只是读请求的处理性能下降
3、Master下线，写请求无法执行
4、其中一台Slave使用SLAVEOF no one命令成为Master，其他Slaves执行SLAVEOF命令指向这个新的Master，从它这里同步数据
```

**演示**

```python
1、启动端口6400redis，设置为6379的slave
   redis-server --port 6400
   redis-cli -p 6400
   redis>slaveof 127.0.0.1 6379
2、启动端口6401redis，设置为6379的slave
   redis-server --port 6401
   redis-cli -p 6401
   redis>slaveof 127.0.0.1 6379
3、关闭6379redis
   sudo /etc/init.d/redis-server stop
4、把6400redis设置为master
   redis-cli -p 6400
   redis>slaveof no one
5、把6401的redis设置为6400redis的salve
   redis-cli -p 6401
   redis>slaveof 127.0.0.1 6400
