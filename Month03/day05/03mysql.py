import pymysql

# 连接数据库
db = pymysql.connect(user="root",
                     password='123456',
                     database="stu",
                     charset="utf8"
                     )

# 创建游标对象: 调用sql语句进行数据操作，得到操作结果的对象
cur = db.cursor()

# 数据操作


# 关闭
cur.close()
db.close()
