import requests

# step 1:指定url
url = 'https://sogou.com/'
# step 2:发送请求
# get方法会返回一个响应对象
response = requests.get(url=url)
# step 3:获取响应数据,text返回的是字符串形式的响应数据
page_text = response.text
print(page_text)
# step 4:持久化存储
with open('./sogou.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
print('结束')
