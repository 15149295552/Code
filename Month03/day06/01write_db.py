"""
多次执行写操作
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

# 数据操作 列表嵌套元素，或者列表套列表
data = [
    ("zhang",'m',17,63),
    ("lisi",'w',18,64),
    ("wang",'m',17,65),
    ("zhao",'w',19,66)
]
try:
    sql="insert into class (name,sex,age,score) values (%s,%s,%s,%s);"
    cur.executemany(sql,data) # 多次执行sql
    db.commit()
except:
    db.rollback()


# 关闭
cur.close()
db.close()
