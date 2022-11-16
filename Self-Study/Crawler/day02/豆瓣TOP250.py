# 拿到网页源代码 requests
# 通过re来提取想要的有效信息
import requests
import re
import csv

url = 'https://movie.douban.com/top250'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
resp = requests.get(url, headers=headers).text
# 解析数据
obj = re.compile(
    r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<fs>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>',
    re.S)
ret = obj.finditer(resp)
f = open('data.csv', 'w', encoding='utf8')
fr = csv.writer(f)
for i in ret:
    # print(i.group('name'))
    # print(i.group('fs'))
    # print(i.group('num'))
    # print(i.group('year').strip())
    dic = i.groupdict()
    dic['year'] = dic['year'].strip()
    fr.writerow(dic.values())
f.close()
print('over')
