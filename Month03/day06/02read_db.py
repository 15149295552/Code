"""
数据库读取操作
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


# 数据读取操作
sql = "select name,age,score from class where score>%s;"
cur.execute(sql, [70])

# 遍历游标
# for row in cur:
#     print(row)

# 通过函数获取指定数量的查询结果
one = cur.fetchone()
print(one)
many = cur.fetchmany(2)
print(many)
all = cur.fetchall()
print(all)

# 关闭
cur.close()
db.close()
