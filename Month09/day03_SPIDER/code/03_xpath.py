import csv
import redis
import requests
import pymysql
from lxml import etree

"""
mysql数据库
create database tmoocdb;
use tmoocdb;
create table tmooctab(
id int primary key auto_increment,
name varchar(200),
number int
);
"""
db = pymysql.connect(host="localhost", user="root", password="123456", database="tmoocdb", charset="utf8")
cur = db.cursor()
ins = "insert into tmooctab(name,number) values(%s,%s)"

"""
存入csv文件
"""
f = open("tmooc.csv", "w")
writer = csv.writer(f)

# 增量爬虫:使用redis
r = redis.Redis()

# 1.请求
url = "https://www.tmooc.cn/free/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
html = requests.get(url=url, headers=headers).content.decode("utf-8", "ignore")

# 2.解析
eobj = etree.HTML(html)
# name_list = eobj.xpath('//h4[@class="bd-tit"]/a/@data-course_name')
# number = eobj.xpath('//div[@class="clearfix"]/span[2]/text()')
li_list = eobj.xpath('//ul[@class="md-bd clearfix md-2018040201-lty"]/li | //ul[@class="hidden-xxw0412 md-bd clearfix md-2018040201-lty"]/li')
for li in li_list:
    href = li.xpath('.//h4/a/@href')[0]
    if r.sadd("tmooc_spider", href) == 0:
        print("已经抓取过")
        continue

    name = li.xpath('.//h4/a/@data-course_name')[0]
    number = li.xpath('.//div[@class="clearfix"]/span[2]/text()')[0]
    number = int(number[:-3].replace(",", ""))

    print(name, number)
    # 存入数据库
    cur.execute(ins, [name, number])
    db.commit()

    # 存入csv文件
    writer.writerow([name, number])

f.close()


# import pandas as pd
#
# df = pd.read_csv("tmooc.csv")
# print(df)

















