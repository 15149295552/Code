"""
    Redis集合实现增量爬虫
"""
import redis
import hashlib
import requests
from lxml import etree

r = redis.Redis()

# 1.请求获取响应
url = "http://news.baidu.com/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"}
html = requests.get(url=url, headers=headers).text

# 2.解析提取数据
eobj = etree.HTML(html)
li_list = eobj.xpath('//div[@class="hotnews"]/ul/li')

for li in li_list:
    href = li.xpath(".//a/@href")[0]
    title = li.xpath(".//a//text()")[0]
    # print(title, href)

    m = hashlib.md5()
    m.update(href.encode())
    finger = m.hexdigest()

    if r.sadd("news:spider", finger) == 1:
        # 新更新新闻,需要抓取
        detail_html = requests.get(url=href, headers=headers).text
        detail_eobj = etree.HTML(detail_html)
        content = detail_eobj.xpath("//article//text()")
        print("抓取新更新的新闻中~~~")
    else:
        # 之前已经抓取过了
        print(f"{title} 已经抓取过")














