import requests

# query = input('搜索内容：')
# url = f'https://sogou.com/web?query={query}'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
# }
# resp = requests.get(url, headers=headers)
# print(resp.text)
# url = 'https://fanyi.baidu.com/sug'
# sug = input('input:')
# params = {
#     'kw': sug
# }
# resp = requests.post(url, params=params)
# print(resp.text)  # 将服务器反水的内容直接处理成json()
url = 'https://movie.douban.com/j/chart/top_list'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
# 重新封装参数
params = {
    'type': 24,
    'interval_id': '100:90',
    'action': '',
    'start': 0,
    'limit': 20,
}
resp = requests.get(url, params=params, headers=headers)
print(resp.json())
resp.close()
