import requests


resp = requests.get(url="https://www.jd.com/",
                    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"})
# text属性: 响应内容 - 字符串
print(resp.text)
# content属性: 响应内容 - bytes 图片、文件、音频、视频
print(resp.content)











