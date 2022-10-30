# 0 导入requests
import requests
import re
import time
import random

# 1 确定url地址
url = 'https://pvp.qq.com/web201605/herolist.shtml'

# (1)构建请求网页的身份信息
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}

# 2 向对应的url地址发送请求
response = requests.get(url, headers=headers)

# (1) 设置响应的编码格式
response.encoding = 'gbk'

# (2) 获取页面的数据
html = response.text
# print(html)

# 3 解析页面数据，获取所有英雄的详细页链接地址
# (1) 解析所有英雄数据存储的数据 <ul>
pattern1 = '<ul class="herolist clearfix">(.*?)</ul>'
list_ul_data = re.findall(pattern1, html, re.S)[0]
# print(list_ul_data)
# print('-' * 60)

# (2) 从ul中的数据解析每个详细页链接地址
pattern = '<a href="(.*?)" target="_blank"'
list_hreo_link = re.findall(pattern, list_ul_data, re.S)
print(list_hreo_link)

# 循环获取多个英雄的详细页
for deal_url in list_hreo_link:
    # 休眠（避免频繁访问，防止IP被禁止）
    time.sleep(random.randint(2, 4))
    # 4 构建详细页完整的URL地址
    hero_link = 'https://pvp.qq.com/web201605/' + deal_url
    print('正在请求：', hero_link)

    # 5 向详细页URL发送请求，获取的页面数据
    response2 = requests.get(hero_link, headers=headers)
    response2.encoding = 'gbk'
    two_page = response2.text

    # 6 解析详细页数据
    # (1) 英雄名字
    name_pattern = '<h2 class="cover-name">(.*?)</h2>'
    hero_name = re.findall(name_pattern, two_page, re.S)[0]
    print(hero_name)

    # (2) 皮肤名字
    pf_pattern = '<ul class="pic-pf-list pic-pf-list3" data-imgname="(.*?)">'
    pf_str = re.findall(pf_pattern, two_page, re.S)[0]
    list_pf_name = [data.split('&')[0] for data in pf_str.split('|')]
    print(list_pf_name)

    # (3) 皮肤图片链接
    img_pattern = '''<div class="zk-con1 zk-con" style="background:url\('(.*?)'\)'''
    img_str = re.findall(img_pattern, two_page, re.S)[0]
    print(img_str)

    # (4) 创建列表存储多个英雄的皮肤图片链接
    list_pf_url = []    # 存储英雄皮肤的链接
    for i in range(len(list_pf_name)):
        img_link = 'https:' + img_str[:-5] + str(i+1) + '.jpg'
        list_pf_url.append(img_link)

    # 7 请求图片的链接地址保存图片
    for i in range(len(list_pf_url)):
        # 休眠（避免频繁访问，防止IP被禁止）
        time.sleep(random.randint(2, 4))
        # 获取图片的字节码数据
        img_data = requests.get(list_pf_url[i], headers=headers).content
        # 保存到本地（文件写入操作）
        file_name = 'C:/Users/16539/Desktop/htSchool/Day21/HeroPF/' + hero_name + '_' + list_pf_name[i] + '.jpg'
        with open(file_name, 'wb') as f:
            f.write(img_data)
        print(f'{file_name}保存成功！！')

"""
1 获取英雄列表页
    目的：获取每个英雄详细页的地址
    实现：
        1 确定英雄列表页的URL地址
        2 构建身份信息，发送get请求，获取响应对象
        3 设置响应的编码格式，通过text属性获取到页面数据
        4 解析页面数据，获取所有英雄的详细页链接地址（存储在列表中）
        
2 遍历请求每个英雄详细页
    目的：从英雄详细页中解析出所有的皮肤图片,并保存到本地
    实现：
        1 构建详细页完整的URL地址
            https://pvp.qq.com/web201605/herodetail/509.shtml
            'https://pvp.qq.com/web201605/' + 'herodetail/506.shtml'
        2 向详细页URL发送请求，获取的页面数据
        3 解析页面数据：
            英雄的名字：<h2 class="cover-name">(.*?)</h2>
            皮肤的名字：<ul class="pic-pf-list pic-pf-list3" data-imgname="(.*?)">
                <ul class="pic-pf-list pic-pf-list3" data-imgname="无尽之盾&0|极冰防御线&0|御銮&48|圆桌骑士&73">
                <ul class="pic-pf-list pic-pf-list3" data-imgname="淬命双剑&0|第七人偶&0|冰霜恋舞曲&5|久胜战神&51|真爱魔法&40|胡桃夹子&50">
                <ul class="pic-pf-list pic-pf-list3" data-imgname="雷霆之王&0|启蛰&0">
            皮肤图片的链接：<div class="zk-con1 zk-con" style="background:url('(.*?)')
                <div class="zk-con1 zk-con" style="background:url('//game.gtimg.cn/images/yxzj/img201606/skin/hero-info/509/509-bigskin-1.jpg') center 0">
                <div class="zk-con1 zk-con" style="background:url('//game.gtimg.cn/images/yxzj/img201606/skin/hero-info/182/182-bigskin-1.jpg') center 0">
        4 请求图片的链接地址保存图片
            1 向图片的链接地址发送请求，获取图片的数据
            2 将图片的数据写入到文件中
"""