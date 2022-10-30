import requests

# 1 确定爬取的URL地址
url = 'https://www.baidu.com'

# 伪装身份信息
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}

# 2 发送请求，获取响应
response = requests.get(url, headers=headers)

# 设置网页编码格式
response.encoding = 'utf-8'

# 获取网页数据
html = response.text
print(html)