import requests

video_url = 'https://vd2.bdstatic.com/mda-nhkb38ytjnc796cr/360p/h264/1661068405944300490/mda-nhkb38ytjnc796cr.mp4?v_from_s=hkapp-haokan-hbe&auth_key=1661681131-0-0-6f53cc0d26bfe60cb860a9644cb5861d&bcevod_channel=searchbox_feed&pd=1&vt=1&cd=0&watermark=0&did=&logid=2131232841&vid=12966074736161214896&pt=0&appver=&model=&cr=0&abtest=peav_l52&sle=1&sl=298&split=323459'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}

video_data = requests.get(video_url, headers=headers).content

with open('好看视频.mp4', 'wb') as f:
    f.write(video_data)