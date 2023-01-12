"""
    定时任务 + 第三方API
"""
import requests
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.blocking import BlockingScheduler


def get_today_temperature():
    """ 获取今天气温 """
    city = "北京"
    # 天气预报请求地址
    url = "http://apis.juhe.cn/simpleWeather/query?city=%s&key=%s" % (city, "5d77cb7936be2bc1e247c46e80a5085d")
    dict_result = requests.get(url).json()
    # {'reason': '查询成功!', 'result': {'city': '北京', 'realtime': {'temperature': '-4', 'humidity': '24', 'info': '多云', 'wid': '01', 'direct': '北风', 'power': '5级', 'aqi': '50'}, 'future': [{'date': '2022-12-15', 'temperature': '-9/-1℃', 'weather': '晴', 'wid': {'day': '00', 'night': '00'}, 'direct': '北风'}, {'date': '2022-12-16', 'temperature': '-12/-2℃', 'weather': '多云转晴', 'wid': {'day': '01', 'night': '00'}, 'direct': '西北风'}, {'date': '2022-12-17', 'temperature': '-11/-4℃', 'weather': '多云', 'wid': {'day': '01', 'night': '01'}, 'direct': '西风转西南风'}, {'date': '2022-12-18', 'temperature': '-10/-2℃', 'weather': '晴', 'wid': {'day': '00', 'night': '00'}, 'direct': '西南风转北风'}, {'date': '2022-12-19', 'temperature': '-9/2℃', 'weather': '晴', 'wid': {'day': '00', 'night': '00'}, 'direct': '北风转南风'}]}, 'error_code': 0}
    dict_current = dict_result["result"]["future"][0]
    # {'date': '2022-12-15', 'temperature': '-9/-1℃', 'weather': '晴', 'wid': {'day': '00', 'night': '00'}, 'direct': '北风'}
    min, max = dict_current["temperature"].split("/")
    print("今天%s,最低%s度,最高%s度,%s,%s" % (
        city, min + "℃", max, dict_current["weather"], dict_current["direct"]))

def main():
    """ 主逻辑 """
    scheduler = BlockingScheduler() # 阻塞
    scheduler.add_job(get_today_temperature, CronTrigger(hour=8,minute=30))
    scheduler.start()

main()



