import requests

url = "https://pics6.baidu.com/feed/09fa513d269759eebdc512f6f1b16a116c22dfc3.jpeg?token=f843200e2087bfeee1e1107f6eb5b239"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

resp = requests.get(url=url, headers=headers).content

with open("liying.jpg", "wb") as f:
    f.write(resp)

# ppt_url = "https://ppt.1ppt.com/uploads/soft/2303/1-23031Q34144.zip"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
#     "Cookie": "mizToken=202303181755090.28999397336649690.33068953155560443; acw_tc=2760826e16791331989005863ec1cb479f0c4372c50adb488c914bd96a3a5f; __bid_n=186f42473995c33e4b4207; FPTOKEN=+FgW9BfDct9O2j0kAq6FpkUn9X2REEDpZKjfLNg0o1TXkJRuL+WuxMFPsCG04V8/a96yCQyuIcHgIC6kUhkWzVkbCvKGJSlmtS2aqNngFAAHH0QZRY4mRK/Z2cYLbwGcJfEWjigK1mKJzi9q60OelHnAfq/ygBPeW3lKyO+CInplM3VPYZGEkKdy2Y0OtjC5O/S5BxHgxOoh9ZqK/FAhZQjZVSQWuS5d5HaI6kQVSYvS4RZO3GJc+p/43sR1GGeslnVmOXVkLwfCUm9EodL+XZwwBj8XSGnYceEo4ub2wrLr2fW348jxXgYE62UcFyLMUXlVseGeGM2moYQOBI3v5dRW2iicF+gjXsJFY3y09vfyLqwUOgZzfV0HKHkNZ2y4gle/qJdaD/6f3EQqQ021fw==|cjXdpIWYqcT5yCcaMcee9ITsZb3d1x/b2/cV6pD2syQ=|10|25b8d69f20e96974d38e78d1df664e12; __51uvsct__Je1p5lxAB8oshp4Q=1; __51vcke__Je1p5lxAB8oshp4Q=ea82cd46-a60a-568e-a78a-c4331572a433; __51vuft__Je1p5lxAB8oshp4Q=1679133278179; __gads=ID=571adf8232e4765a-224e8fe27bdc0067:T=1679133208:RT=1679133208:S=ALNI_MbTNj5QppVjTekh_kYwcjntqJMEBg; __gpi=UID=00000bdb31549ce4:T=1679133208:RT=1679133208:S=ALNI_MbhZQrN4UUFFNgB_dZg_iY7K1m2JQ; __vtins__Je1p5lxAB8oshp4Q=%7B%22sid%22%3A%20%227cdc5372-ff8b-52b3-8534-4d06bf61febb%22%2C%20%22vd%22%3A%204%2C%20%22stt%22%3A%2025226%2C%20%22dr%22%3A%205654%2C%20%22expires%22%3A%201679135103401%2C%20%22ct%22%3A%201679133303401%7D",
# }
#
# ppt_resp = requests.get(url=ppt_url, headers=headers).content
#
# with open("ppt.zip", "wb") as f:
#     f.write(ppt_resp)


