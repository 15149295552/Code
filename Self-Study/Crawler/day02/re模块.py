import re

# findall:匹配字符串中所有的符合正则的内容
# rst = re.findall(r'\d+', '我的电话号是10086')
# print(rst)
# # finditer：匹配字符串中所有的内容[返回的是迭代器]
# rst1 = re.finditer(r'\d+', '我的100，你的111')
# for i in rst1:
#     print(i.group())
# # search返回的结果是match对象，拿数据需要.group()
# rst2 = re.search(r'\d+', '我的100，你的111')
# print(rst2.group())
# # match从头开始匹配
# rst3 = re.match(r'\d+', '100，你的111')
# print(rst3.group())
# 预加载正则表达式
# obj = re.compile(r'\d+')
# rst = obj.finditer('我的100，你的111')
# for it in rst:
#     print(it.group())
#
# rst = obj.findall('我的111000')
# print(rst)
s = """
<div class="jay"><span id="1">郭麒麟</span></div>
<div class="jj"><span id="2">宋铁</span></div>
<div class="jolin"><span id="3">大聪明</span></div>
<div class="jylar"><span id="4">范思哲</span></div>
<div class="tory"><span id="5">胡说八道</span></div>
"""
# (?P<分组名字>正则)可以单独从正则匹陪的内容中进一步提取内容
obj = re.compile(r'<div class=".*?"><span id="(?P<id>\d+)">(?P<re>.*?)</span></div>', re.S)  # re.S:让.能匹配换行符
ret = obj.finditer(s)
for i in ret:
    print(i.group('id', 're'))
    # print(i.group('re'))
