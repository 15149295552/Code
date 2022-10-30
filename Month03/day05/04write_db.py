"""
数据库写操作
程序执行自动开启事务，如果数据表支持事务则需要
commit提交。如果数据表不支持事务则execute后
直接生效
"""
import pymysql

# 连接数据库
db = pymysql.connect(user="root",
                     password='123456',
                     database="stu",
                     charset="utf8"
                     )

# 创建游标对象: 调用sql语句进行数据操作，得到操作结果的对象
cur = db.cursor()

# 数据写操作 insert delete update
id = input("ID:")
sc = input("Score:")
try:
    sql = "update class set score=%s where id=%s;"
    cur.execute(sql, [sc, id])  # 给sql传值
    sql = "delete from class where score <60;"
    cur.execute(sql)  # 执行sql语句
    db.commit()  # 提交事务
except:
    # 如果出现异常，捕获异常，继续向下执行
    db.rollback()  # 事务回滚

print("继续执行其他代码....")

# 关闭
cur.close()
db.close()
