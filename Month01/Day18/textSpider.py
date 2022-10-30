import requests
import re

url = 'https://www.17k.com/chapter/3381946/45309702.html'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}

text_data = requests.get(url, headers=headers).content.decode('utf-8')
# print(text_data)

title_pattern = '<h1>(.*?)</h1>'
title = re.findall(title_pattern, text_data)[0]

content_pattern = '<div class="p">(.*?)</div>'
text = re.findall(content_pattern, text_data, re.S)[0].strip()
print(title, text)

text = text.replace('<p>', '').replace('</p>', '\n\n').replace('\n', '').replace('\t', '')

with open('小说.txt', 'w', encoding='utf-8') as f:
    f.write(text)