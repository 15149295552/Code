from urllib.request import urlopen

url = 'http://www.baidu.com'
resp = urlopen(url)
with open('mybaidu.html', 'w', encoding='utf8') as f:
    f.write(resp.read().decode('utf-8'))  # 读取到网页的页面源代码
print('over')
