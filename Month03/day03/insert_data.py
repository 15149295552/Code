"""
use stu;
create table index_test (id int primary key auto_increment,name varchar(30));
"""

import pymysql

db = pymysql.connect(user='root',password="123456",database='stu',charset='utf8')

cur = db.cursor()

sql = "insert into index_test (name) values (%s);"
exe = []
s = "Tom"
for i in range(1,2000001):
    name = s + str(i)
    exe.append(name)


try:
    cur.executemany(sql,exe)
    db.commit()
except:
    db.rollback()

db.close()

