"""
建立数据库 dict
在该数据库下建立数据表 words
id   word  mean

create database dict;
create table words (id int primary key
auto_increment,word varchar(30),mean text);

编程将dict.txt中的单词插入数据表
"""
import pymysql


class Dict:
    def __init__(self):
        self.db = pymysql.connect(user="root", password='123456', database="dict", charset="utf8")
        self.cur = self.db.cursor()

    # 关闭
    def close(self):
        self.cur.close()
        self.db.close()

    # 提取数据  dict.txt --> [(word,mean),()....]
    def get_data(self):
        data = []
        with open("dict.txt", 'r') as fr:
            for line in fr:
                word, mean = line.split(' ', 1)
                data.append((word, mean.strip()))
        return data

    # 数据写操作 insert  data-> [(word,mean),()....]
    def insert_words(self):
        data = self.get_data()  # 获取数据
        try:
            for word, mean in data:
                sql = "insert into words (word,mean) values (%s,%s);"
                self.cur.execute(sql, [word, mean])
            self.db.commit()  # 提交事务
        except:
            self.db.rollback()  # 事务回滚


if __name__ == '__main__':
    dict = Dict()
    dict.insert_words()
    dict.close()








# def get_word_and_mean(info):
#     info = "a                indef art one"
#     flag = 1 # 标志变量
#     word = "" # 累加单词
#     for i in range(len(info)):
#         if info[i] != " " and flag:
#             word += info[i] # 单词
#         elif info[i] != " " and flag == 0:
#             mean = info[i:] # 获取解释
#             break
#         else:
#             flag = 0 # 单词与解释之间的空格
#     return word,mean
#
# res = get_word_and_mean("")
# print(res)
