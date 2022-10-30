"""
数据处理 与数据库交互
1. 根据服务端的需要进行数据的读写操作 （类）
"""
import pymysql
import hashlib


# 数据库交互
class Dict:
    # 密码加密方法
    @staticmethod
    def encryp(pwd):
        hash = hashlib.sha256()  # 选择算法
        hash.update(pwd.encode())  # 转换加密
        return hash.hexdigest()  # 获取结果

    def __init__(self, **kwargs):
        self.db = pymysql.connect(**kwargs)
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    # -- 以下函数 根据 服务端的业务需要 编写----
    def register(self, user, pwd):
        pwd = self.encryp(pwd)  # 密码转换
        sql = "insert into user (user,password) value (%s,%s);"
        try:
            self.cur.execute(sql, [user, pwd])
            self.db.commit()
            return True
        except:
            self.db.rollback()

    def login(self, user, pwd):
        pwd = self.encryp(pwd)
        sql = "select id from user where user=%s and password=%s;"
        self.cur.execute(sql, [user, pwd])
        return self.cur.fetchone()  # (id,) None

    def search(self, word):
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql, [word])
        return self.cur.fetchone()  # (mean,) ()


if __name__ == '__main__':
    dict = Dict(user="root", password="123456",
                database="dict", charset="utf8")
    # 干事

    dict.close()
