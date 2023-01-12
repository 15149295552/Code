"""

"""
from datetime import datetime, timedelta

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.date import DateTrigger
from apscheduler.triggers.interval import IntervalTrigger


def print_hello_world():
    print("hello_world")

# 后台调度器(大项目)
# scheduler = BackgroundScheduler()
# 阻塞性调度器(定时任务项目)
scheduler = BlockingScheduler()

# 间隔触发器
# 注意：只写函数名称,不要括号
# scheduler.add_job(print_hello_world, IntervalTrigger(seconds=2))
# 每天18点触发
# scheduler.add_job(print_hello_world, CronTrigger(hour=18))

# 测试
# scheduler.add_job(print_hello_world, CronTrigger(second=1))
# scheduler.add_job(print_hello_world, IntervalTrigger(seconds=1))

# scheduler.add_job(print_hello_world, DateTrigger(datetime.now() + timedelta(seconds=3)))
scheduler.start()

print("后续逻辑")