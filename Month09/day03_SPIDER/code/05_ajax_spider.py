import sys
import json
import random
import time
from lxml import etree
import requests
from fake_useragent import UserAgent


class DouBanSpider:
    def __init__(self):
        pass

    def get_headers(self):
        """
        功能函数:生成随机请求头中的User-Agent
        :return: headers
        """
        return {"User-Agent": UserAgent().random}

    def get_html(self, url):
        """
        功能函数: 获取响应内容html
        :param url: 请求的url地址
        :return: html
        """
        return requests.get(url=url, headers=self.get_headers()).text

    def parse_html(self, url):
        """
        抓取数据的函数
        :return:
        """
        # html: "[{},{},...]"
        html = self.get_html(url=url)
        # html: [{},{},...]
        html = json.loads(html)
        for dic in html:
            item = {}
            item["rank"] = dic.get("rank")
            item["title"] = dic.get("title")
            item["score"] = dic.get("score")
            item["release_date"] = dic.get("release_date")
            print(item)

    def get_total(self, type_value):
        """
        功能函数：获取电影总数
        :return:
        """
        total_url = f"https://movie.douban.com/j/chart/top_list_count?type={type_value}&interval_id=100%3A90"
        total_html = self.get_html(url=total_url)
        total_html = json.loads(total_html)

        return total_html.get("total")

    def get_type_dict(self):
        """
        功能函数：获取类型和type值的字典
        :return:
        """
        type_url = "https://movie.douban.com/chart"
        type_html = self.get_html(url=type_url)
        # 解析提取数据
        type_dict = {}
        eobj = etree.HTML(type_html)
        href_list = eobj.xpath('//div[@class="types"]/span/a/@href')
        for href in href_list:
            # /typerank?type_name=剧情&type=11&interval_id=100:90&action=
            key = href.split("&")[0].split("=")[1]
            value = href.split("&")[1].split("=")[1]
            type_dict[key] = value

        return type_dict

    def crawl(self):
        """
        程序入口函数
        :return:
        """
        # {"剧情":"11", "喜剧":"24", ...}
        type_dict = self.get_type_dict()
        menu = "|".join(type_dict.keys())
        print(menu)
        choice = input("请选择:")
        # 判断类型是否正确
        if choice not in type_dict:
            # 彻底退出进程(结束程序)
            sys.exit("类型错误!")

        # 获取type的值
        type_value = type_dict.get(choice)
        # 获取电影总数
        total = self.get_total(type_value)
        for start in range(0, total, 20):
            page_url = f"https://movie.douban.com/j/chart/top_list?type={type_value}&interval_id=100%3A90&action=&start={start}&limit=20"
            self.parse_html(url=page_url)
            # 控制频率
            time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    spider = DouBanSpider()
    spider.crawl()







