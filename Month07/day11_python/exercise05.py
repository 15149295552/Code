"""
    练习1：每天16点执行一次

    练习2：每1小时执行一次

    练习3：延迟1分钟执行
"""
from datetime import datetime, timedelta

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.date import DateTrigger

def job():
    print("执行啦")

scheduler = BlockingScheduler() # 阻塞
scheduler.add_job(job, CronTrigger(hour=16))
scheduler.add_job(job, IntervalTrigger(hours=1))
scheduler.add_job(job, DateTrigger(datetime.now() + timedelta(minutes=1)))
scheduler.start()